# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class FajnBrigadyItem(scrapy.Item):
    type = scrapy.Field()
    name = scrapy.Field()
    link = scrapy.Field()
    caption = scrapy.Field()
    picture = scrapy.Field()
    description = scrapy.Field()


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


