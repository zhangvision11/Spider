# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonUsItem(scrapy.Item):
    price = scrapy.Field()
    zuozhe = scrapy.Field()
    shangBiao = scrapy.Field()
    sjTime = scrapy.Field()
    stars = scrapy.Field()
    haoPing = scrapy.Field()
    chaPing = scrapy.Field()
    hpdzs = scrapy.Field()
