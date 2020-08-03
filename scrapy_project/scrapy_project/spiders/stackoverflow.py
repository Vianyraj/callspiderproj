# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from ..items import EventItemBmbf, EventItemWiki
from questions.models import Paper_model

class SpiderBmbf(scrapy.Spider):    #Spider for BMBF
    name = "CrawlerBmbf"
    start_urls = ['https://www.bmbf.de/foerderungen/']

    def parse(self, response):
        loader = ItemLoader(item=EventItemBmbf(), response=response)
        loader.add_xpath("TitleBMBF",'//article[@class="block-teaser block-teaser--noimage"][@role="article"]/div[@class="teaser-content"]//h3/text()')
        loader.add_xpath("DatesBMBF",'//article[@class="block-teaser block-teaser--noimage"][@role="article"]/div[@class="teaser-content"]//p[@class="meta-date"]/text()')
        loader.add_xpath("UrlBMBF",'//article[@class="block-teaser block-teaser--noimage"][@role="article"]/div[@class="teaser-content"]//p[@class="readmore-wrap"]/a[@class="icon-link"]/@href')

        #store crawled data in a dict, then yield it to pipeline
        item = loader.load_item()
        BMBFDOMAIN = 'https://www.bmbf.de/'

        for k in range(int(len(item["TitleBMBF"]))):
            yield {"title": item["TitleBMBF"][k],
                   "date": item["DatesBMBF"][k],
                   "url": BMBFDOMAIN + item["UrlBMBF"][k],
                   "paperType": "BMBF",
                   "where": None,
                   "deadline": None
            }



class SpiderWiki(scrapy.Spider):     #Spider for Wiki
    name = "CrawlerWiki"
    start_urls = ['http://www.wikicfp.com/cfp/']

    def parse(self, response):
        loader = ItemLoader(item=EventItemWiki(), response=response)
        loader.add_xpath("Titlewiki", '//td[@colspan="3"]//td[@align="left"]/text()')
        loader.add_xpath("Urlwiki", '//td[@colspan="3"]//td[@rowspan="2"][@align="left"]//a/@href')

        #store crawled data in a dict, then yield it to pipeline
        item = loader.load_item()
        WIKIDOMAIN = 'http://www.wikicfp.com'
        i = 0
        for h in range(int(len(item["Titlewiki"]) / 4)):
            yield {"title":item["Titlewiki"][i],
                   "date":item["Titlewiki"][i + 1],
                   "url":WIKIDOMAIN + item["Urlwiki"][h],
                   "paperType":"Wiki",
                   "where": item["Titlewiki"][i + 2],
                   "deadline": item["Titlewiki"][i + 3],
            }
            i = i + 4
