# -*- coding: utf-8 -*-
from datetime import datetime

import scrapy
from scrapy.loader import ItemLoader
#from scrapy_django.scrapy_project.scrapy_project.items import EventItemBmbf, EventItemWiki
from ..items import EventItemBmbf, EventItemWiki
from scrapy.crawler import CrawlerProcess

from scrapy_project.scrapy_project.pipelines import ScrapyProjectPipeline #will be delete
from dateutil.parser import parse
class SpiderBmbf(scrapy.Spider):    #Spider for BMBF
    name = "SpiderBmbf"
    start_urls = ['https://www.bmbf.de/foerderungen/']
    TitleXpath = '//article[@class="block-teaser block-teaser--noimage"][@role="article"]/div[@class="teaser-content"]//h3/text()'
    DateXpath = '//article[@class="block-teaser block-teaser--noimage"][@role="article"]/div[@class="teaser-content"]//p[@class="meta-date"]/text()'
    UrlXpath = '//article[@class="block-teaser block-teaser--noimage"][@role="article"]/div[@class="teaser-content"]//p[@class="readmore-wrap"]/a[@class="icon-link"]/@href'
    def parse(self, response):
        print(self.TitleXpath)

        if response.xpath(self.TitleXpath).get() is None \
            or response.xpath(self.DateXpath) is None\
            or response.xpath(self.UrlXpath) is None:
            print("xpath has changed")
            raise ValueError("the webpage has changed")



        loader = ItemLoader(item=EventItemBmbf(), response=response)
        loader.add_xpath("TitleBMBF",self.TitleXpath)
        loader.add_xpath("DateBMBF",self.DateXpath)
        loader.add_xpath("UrlBMBF",self.UrlXpath)#//div[@class="main"]//div[@class="content"]//div[@class="article-section"]//p/strong
        #response.xpath('//div[@class="main"]//div[@class="content"]//div[@class="article-section"]//p/strong/text()')[0].extract()
        item = loader.load_item()
        #date: //div[@class="main"]//div[@class="content"]//span[@class="datum"]
        #date and title # response.xpath('//article[@class="block-teaser block-teaser--noimage"][@role="article"]/div[@class="teaser-content"]//p/text()')[5].extract()
        #//article[@class="block-teaser block-teaser--noimage"][@role="article"]/div[@class="teaser-content"]//p
        if "TitleBMBF" not in item or "DateBMBF" not in item or "UrlBMBF" not in item :
            print("item is not loaded properly")
            raise ValueError("the webpage has changed")

        #store crawled data in a dict, then yield it to pipeline
        mydict={"title": [],
                "date":[],
                "url": [],
                "paperType": [],
                "where": [],
                "deadline": []
                }
        #print(item["DateBMBF"])

        for k in range(int(len(item["TitleBMBF"]))):

            mydict["title"].append(item["TitleBMBF"][k])
            mydict["date"].append( datetime.strptime( item["DateBMBF"][k].replace(" ","").split("-")[0], '%d.%m.%Y'))
            mydict["url"].append('https://www.bmbf.de/' + item["UrlBMBF"][k])
            mydict["paperType"].append("BMBF")
            mydict["where"].append(None)
            if (len(item["DateBMBF"][k].split("-"))>1):
                #if formatchecker!=datetime.strptime( (item["DateBMBF"][k].replace(" ","")).split("-")[1], '%d.%m.%Y')
                    #raise ValueError("the webpage has changed or the date format has changed")
                print(datetime.strptime( (item["DateBMBF"][k].replace(" ","")).split("-")[1], '%d.%m.%Y'))
                mydict["deadline"].append( datetime.strptime( (item["DateBMBF"][k].replace(" ","")).split("-")[1], '%d.%m.%Y'))

            else:
                mydict["deadline"].append(None)
        #print(item["UrlBMBF"])
        # for k in range(int(len(item["TitleBMBF"]))):
        #     mydict= {"title":item["TitleBMBF"][k],
        #            "date":item["DateBMBF"][k],
        #            "url":"https://www.bmbf.de/" + item["UrlBMBF"][k],
        #            "paperType":"Bmbf",
        #            "where": None,
        #            "deadline": None,
        #     }

        print("mydict")
        print("..................................................")
        #Calling pipeline inside will call pipeline 20 times
        myPipeline=ScrapyProjectPipeline()
        myPipeline.process_item(mydict,SpiderBmbf)
        yield mydict #if we put this outside for loop calling pipelines 1 times


class SpiderWiki(scrapy.Spider):     #Spider for Wiki
    name = "SpiderWiki"
    start_urls = ['http://www.wikicfp.com/cfp/']
    TitleXpath= '//td[@colspan="3"]//td[@align="left"]//text()'
    DateXpath= '//td[@colspan="3"]//td[@align="left"][1]/text()'
    UrlXpath ='//td[@colspan="3"]//td[@rowspan="2"][@align="left"]//a/@href'
    DeadlineXpath= '//td[@colspan="3"]//td[@align="left"][3]/text()'
    PlaceXpath='//td[@colspan="3"]//td[@align="left"][last()-1]/text()'

    def parse(self, response):
        #print(type(response))
        if response.xpath(self.DateXpath).get() is None \
            or response.xpath(self.UrlXpath) is None\
            or response.xpath(self.DeadlineXpath) is None\
            or response.xpath(self.PlaceXpath)  is None \
            or response.xpath(self.TitleXpath) is None    :

            raise ValueError("the webpage has changed")


        loader = ItemLoader(item=EventItemWiki(), response=response) #loader of type EventItemWiki
        loader.add_xpath("DateWiki", self.DateXpath)
        loader.add_xpath("UrlWiki", self.UrlXpath)
        loader.add_xpath("DeadlineWiki", self.DeadlineXpath)
        loader.add_xpath("PlaceWiki", self.PlaceXpath)
        #loader.add_xpath("TitleWiki",'//td[@colspan="3"]//td[@align="left"]//text()')
        j=0
        for i in range(int(len(loader.load_item()["PlaceWiki"]) )):
            title=response.xpath(self.TitleXpath)[j+1].extract()
            loader.add_value("TitleWiki", title )
            j=j+5

        item = loader.load_item()  # item is loaded with loader data dictionary
        #print(item)

        if "TitleWiki" not in item or "DateWiki" not in item or "UrlWiki" not in item or "DeadlineWiki" not in item or "PlaceWiki" not in item: #you do it
            print("item is not loaded properly")
            raise ValueError


        #store crawled data to a dict, then yield to pipeline #calling pipelines 1 times
        mydict={"title": [],
                "date":[],
                "url": [],
                "paperType": [],
                "where": [],
                "deadline": []
                }

        for k in range(int(len(item["TitleWiki"]))):
            mydict["title"].append(item["TitleWiki"][k])
            mydict["date"].append(item['DateWiki'][k].split("-")[0][0:12].rstrip())
            mydict["url"].append('http://www.wikicfp.com' + item["UrlWiki"][k])
            mydict["paperType"].append("Wiki")
            mydict["where"].append(item["PlaceWiki"][k])
            #mydict["deadline"].append(item["DeadlineWiki"][k])
            print("---------------------------------------------")
            print(item["DateWiki"][k])
            print('.' + item['DateWiki'][k].split("-")[0][0:12].rstrip() + ".")
            print(item['DeadlineWiki'][k])
            if (item["DeadlineWiki"][k]=="TBD"):#TBD
                mydict["deadline"].append(item["DeadlineWiki"][k])
            elif (len(item["DeadlineWiki"][k])>=12): #with brackets
                mydict["deadline"].append(item['DeadlineWiki'][k].split("(")[0][0:12].rstrip())
                print('.'+item['DeadlineWiki'][k].split("(")[0][0:12].rstrip()+".")
                #datetime.strptime(item['DeadlineWiki'][k].split("(")[0][0:12].rstrip(), '%b %d, %Y')

            else: # normal case
                print(datetime.strptime(item['DeadlineWiki'][k],'%b %d, %Y'))
                mydict["deadline"].append(datetime.strptime(item['DeadlineWiki'][k],'%b %d, %Y'))




        #Calling pipeline
        myPipeline = ScrapyProjectPipeline()
        myPipeline.process_item(mydict, SpiderWiki)
        yield mydict#calling pipelines 1 times



        # for h in range(int(len(item["TitleWiki"]))):#calling pipelines 20 times
        #     yield {"title":item["TitleWiki"][i],
        #            "date":item["DateWiki"][i],
        #            "url":'http://www.wikicfp.com' + item["UrlWiki"][h],
        #            "paperType":"Wiki",
        #            "where": item["PlaceWiki"][i],
        #            "deadline": item["DeadlineWiki"][i ],
        #     }
        #
        #     myPipeline = ScrapyProjectPipeline()
        #     myPipeline.process_item(mydict, SpiderWiki)

#calling 20 times we call pipelines outside for loop
# calling 1 time we call pipeline inside for loop.

