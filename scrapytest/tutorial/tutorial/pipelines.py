# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os

import pymongo
from scrapy.exceptions import DropItem
import facebook


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class PricePipeline(object):
    """
    Price validation and dropping items with no prices
    """
    vat_factor = 1.15

    def process_item(self, item, spider):
        if item['price']:
            if item['price_exludes_vat']:
                item['price'] = item['price'] * self.vat_factor
            return item
        else:
            raise DropItem("Missing price in %s" % item)


class JsonWriterPipeline(object):
    """
    Write items to a JSON file
    """

    def __init__(self):
        self.file = open('items.jl', 'wb')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.unlink(self.file)

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        # if not hasattr(self, 'file'):
        #     self.file = open('items.jl', 'wb')

        self.file.write(bytes(line, 'UTF-8'))
        return item


class MongoPipeline(object):
    collection_name = 'scrapy_items'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(dict(item))
        return item


class FacebookPipeline(object):
    def __init__(self, fb_user_token):
        print(fb_user_token)
        self.fb_user_token = fb_user_token

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            fb_user_token=crawler.settings.get('FACEBOOK_USER_TOKEN')
        )

    def open_spider(self, spider):
        self.graph = facebook.GraphAPI(access_token=self.fb_user_token, version='2.6')

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.graph.put_wall_post(message='Fajn brigáda nabzí', attachment=item)


class DuplicatesPipeline(object):
    def __init__(self):
        self.ids_seen = sorted(set(), reverse=True)

    def process_item(self, item, spider):
        if item['title'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.append(item['title'])
            return item
