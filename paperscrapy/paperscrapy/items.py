# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PaperscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    Eventnamelink = scrapy.Field()
    Eventname = scrapy.Field()
    whenlink = scrapy.Field()
    when = scrapy.Field()

    pass
