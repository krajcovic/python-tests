#!/usr/bin/python3
# -*- coding: utf-8 -*-

import scrapy

from scrapy.shell import inspect_response

from ..items import FajnBrigadyItem

class FajnBrigadySpider(scrapy.Spider):
    name = 'fajnbrigady'
    start_urls = ['http://www.fajn-brigady.cz/brigady/zlin/']

    def parse(self, response):
        for href in response.css('.titulek1 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        # inspect_response(response, self)

        item = FajnBrigadyItem

        # S obrazkem
        # if response.xpath("boolean(//*[contains(@class, 'nazev-pozice')])"):
        if response.xpath("boolean(//*[contains(@class, 'nazev-pozice')])").extract() == ['1']:
            item = {
                'name': response.xpath("//*[contains(@class, 'nazev-pozice')]").extract(),
                'link': response.url,
                'caption': response.xpath("//table[@class='detail-zvyhodnena-firma']/tr[3]/td/p/text()").extract(),
                'picture': response.xpath("//table[@class='hlavicka']/tr/td/a/img/@src").extract(),
                'description': response.xpath("//table[@class='detail-zvyhodnena-firma']/tr[3]/td/p/text()").extract()
            }

        # Bez obrazku
        # if response.xpath("boolean(//h1[@class='detail']/span/text())").extract():
        if response.xpath("boolean(//h1[@class='detail']/span/text())").extract() == ['1']:
            item = {
                'name': response.xpath("//h1[@class='detail']/span/text()").extract(),
                'link': response.url,
                'caption': response.xpath("//div[@class='text']/text()").extract_first(),
                'picture': 'http://www.fajn-brigady.cz/img/front/fb-logo.png',
                'description': response.xpath("//div[@class='text']/text()").extract()[1:]
            }

        yield item
