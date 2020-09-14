#-*- coding: utf-8 -*-
#import scrapy
#from ..items import PaperscrapyItem
#from scrapy.loader import ItemLoader
# import numpy as np
# from scrapy_djangoitem import DjangoItem


#
# class PaperSpiderSpider(scrapy.Spider):
#     name = 'paper'
#     #allowed_domains = ['paper.com']
#     #start_urls = ['https://en.wikipedia.org/wiki/Mercedes-Benz_Sprinter']
#     #start_urls = ['https://ieeexplore.ieee.org/Xplore/home.jsp']
#     #start_urls = ['https://www.bmbf.de/foerderungen/']
#     start_urls = ['http://www.wikicfp.com/cfp/']
#     #start_urls = ['http://quotes.toscrape.com/']
#
#     def parse(self, response):
#
#          items = PaperscrapyItem()
#          loader = ItemLoader(item=PaperscrapyItem(),response=response)
#          loader.add_xpath("when", "//tr[@bgcolor='#f6f6f6']/td[@align='left']/text()")
#          loader.add_xpath("Eventname", "//tr[@bgcolor='#e6e6e6']/td[@align='left']/text()")
#          loader.add_xpath("whenlink",'//tr[@bgcolor="#f6f6f6"]/td[@rowspan="2"][@align="left"]/a/@href')
#          loader.add_xpath("Eventnamelink",'//tr[@bgcolor="#e6e6e6"]/td[@rowspan="2"][@align="left"]/a/@href')
#          #loader.add_xpath("Eventall",'//td[@colspan="3"]//td[@align="left"]')
#          #loader.add_xpath("Alllink",'//td[@colspan="3"]//td[@rowspan="2"][@align="left"]//a/@href')
#          yield loader.load_item()




#https://blog.theodo.com/2019/01/data-scraping-scrapy-django-integration/


import scrapy
from ..items import TheodoTeamItem

class TheodoSpider(scrapy.Spider):
      name = "theodo"
      start_urls = ["https://www.theodo.co.uk/team"]

      # this is what start_urls does123
      # def start_requests(self):
      #     urls = ['https://www.theodo.co.uk/team',]
      #     for url in urls:
      #       yield scrapy.Request(url=url, callback=self.parse)

      def parse(self, response):
          data = response.css("div.st-about-employee-pop-up")

          for line in data:
              item = TheodoTeamItem()
              item["name"] = line.css("div.h3 h3::text").extract_first()
              item["image"] = line.css("img.img-team-popup::attr(src)").extract_first()
              item["fun_fact"] = line.css("div.p-small p::text").extract().pop()
              yield item