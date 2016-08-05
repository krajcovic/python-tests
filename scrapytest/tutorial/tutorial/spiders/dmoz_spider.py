#!/usr/bin/python3
# -*- coding: utf-8 -*-

import scrapy
from scrapy.shell import inspect_response

from ..items import DmozItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        # inspect_response(response, self)
        for site_item in response.xpath("//div[@class='site-item ']"):
            item = DmozItem()
            item['title'] = site_item.xpath("div[@class='title-and-desc']/a/div[@class='site-title']/text()").extract()
            item['link'] = site_item.xpath("div[@class='title-and-desc']/a/@href").extract()
            item['desc'] = site_item.xpath(
                "div[@class='title-and-desc']/div[@class='site-descr ']/text()").extract()
            yield item

            # def parse_old(self, response):
            #     # inspect_response(response, self)
            #     filename = response.url.split("/")[-2] + '.html'
            #     with open(filename, 'wb') as f:
            #         f.write(response.body)
