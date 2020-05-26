# -*- coding: utf-8 -*-
import scrapy
from ..items import PaperscrapyItem
from scrapy.loader import ItemLoader
import numpy as np

class PaperSpiderSpider(scrapy.Spider):
    name = 'paper'
    #allowed_domains = ['paper.com']
    #start_urls = ['https://en.wikipedia.org/wiki/Mercedes-Benz_Sprinter']
    #start_urls = ['https://ieeexplore.ieee.org/Xplore/home.jsp']
    #start_urls = ['https://www.bmbf.de/foerderungen/']
    start_urls = ['http://www.wikicfp.com/cfp/']
    #start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):

         items = PaperscrapyItem()

         loader = ItemLoader(item=PaperscrapyItem(),response=response)
         loader.add_xpath("when", "//tr[@bgcolor='#f6f6f6']/td[@align='left']/text()")
         loader.add_xpath("Eventname", "//tr[@bgcolor='#e6e6e6']/td[@align='left']/text()")
         loader.add_xpath("whenlink",'//tr[@bgcolor="#f6f6f6"]/td[@rowspan="2"][@align="left"]/a/@href')
         loader.add_xpath("Eventnamelink",'//tr[@bgcolor="#e6e6e6"]/td[@rowspan="2"][@align="left"]/a/@href')

         yield loader.load_item()
