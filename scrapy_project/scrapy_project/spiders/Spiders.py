# -*- coding: utf-8 -*-
from datetime import datetime, date

import scrapy
from scrapy.loader import ItemLoader
from ..items import EventItemBmbf, EventItemWiki

from scrapy_project.scrapy_project.pipelines import ScrapyProjectPipeline



class SpiderBmbf(scrapy.Spider):    #Spider for BMBF
    name = "SpiderBmbf"
    start_urls = ['https://www.bmbf.de/foerderungen/']
    TitleXpath = '//div[@class="teaser-content"]//a//p/text()'
    DateXpath = '//div[@class="main"]//div[@class="content"]//div[@class="teaser-meta"]//p[@class="meta-date"]/text()'
    UrlXpath = '//div[@class="teaser-content"]//a/@href'



    def parse(self, response):


        if response.xpath(self.TitleXpath).get() is None:
            raise ValueError("the TitleXpath of Bmbf webpage has changed")
        elif response.xpath(self.DateXpath).get() is None :
            raise ValueError("the Bmbf webpage xpath has changed")
        elif response.xpath(self.UrlXpath).get() is None:
            raise ValueError("the URl of Bmbf webpage xpath has changed")


        loader = ItemLoader(item=EventItemBmbf(), response=response)
        loader.add_xpath("TitleBMBF",self.TitleXpath)
        loader.add_xpath("DateBMBF",self.DateXpath)
        loader.add_xpath("UrlBMBF",self.UrlXpath)#//div[@class="main"]//div[@class="content"]//div[@class="article-section"]//p/strong
        item = loader.load_item()
        #
        if "TitleBMBF" not in item :
            raise ValueError("TitleBMBF item is not loaded")
        elif "DateBMBF" not in item:
            raise ValueError("DateBMBF item is not loaded")
        elif "UrlBMBF" not in item :
            raise ValueError("UrlBMBF item is not loaded")


        #store crawled data in a dict, then yield it to pipeline
        mydict={"title": [],
                "date":[],
                "url": [],
                "paperType": [],
                "where": [],
                "deadline": []
                }


        for k in range(int(len(item["UrlBMBF"]))):

            mydict["title"].append(item["TitleBMBF"][k])
            mydict["date"].append( datetime.strptime( item["DateBMBF"][k].replace(" ","").split("-")[0], '%d.%m.%Y'))
            #print("date",datetime.strptime( item["DateBMBF"][k].replace(" ","").split("-")[0], '%d.%m.%Y'))
            #print("----------------------")
            mydict["url"].append('https://www.bmbf.de/' + item["UrlBMBF"][k])

            if (len(item["DateBMBF"][k].split("-"))>1):
                #if formatchecker!=datetime.strptime( (item["DateBMBF"][k].replace(" ","")).split("-")[1], '%d.%m.%Y')
                    #raise ValueError("the webpage has changed or the date format has changed")
                #print(datetime.strptime( (item["DateBMBF"][k].replace(" ","")).split("-")[1], '%d.%m.%Y'))
                mydict["deadline"].append( datetime.strptime( (item["DateBMBF"][k].replace(" ","")).split("-")[1], '%d.%m.%Y'))

            else:
                mydict["deadline"].append(None)



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
        print("typeeeeeeeeeeeeeeeeeeeeeee",response)
        print("typeeeeeeeeeeeeeeeeeeeeeee", type(response))
        # if response.xpath(self.DateXpath).get() is None \
        #     or response.xpath(self.UrlXpath).get() is None\
        #     or response.xpath(self.DeadlineXpath).get() is None\
        #     or response.xpath(self.PlaceXpath).get()  is None \
        #     or response.xpath(self.TitleXpath).get() is None    :
        #
        #     raise ValueError("Wiki webpage has changed")
        if response.xpath(self.DateXpath).get() is None:
            raise ValueError("the DateXpath of Wiki webpage has changed")
        if response.xpath(self.UrlXpath).get() is None:
            raise ValueError("the UrlXpath of Wiki webpage has changed")
        if response.xpath(self.DeadlineXpath).get() is None:
            raise ValueError("the DeadlineXpath of Wiki webpage has changed")
        if response.xpath(self.PlaceXpath).get() is None:
            raise ValueError("the PlaceXpath of Wiki webpage has changed")
        if response.xpath(self.TitleXpath).get() is None:
            raise ValueError("the TitleXpath of Wiki webpage has changed")



        loader = ItemLoader(item=EventItemWiki(), response=response) #loader of type EventItemWiki
        loader.add_xpath("DateWiki", self.DateXpath)
        loader.add_xpath("UrlWiki", self.UrlXpath)
        loader.add_xpath("DeadlineWiki", self.DeadlineXpath)
        loader.add_xpath("PlaceWiki", self.PlaceXpath)
        j=0
        for i in range(int(len(loader.load_item()["PlaceWiki"]) )):
            title=response.xpath(self.TitleXpath)[j+1].extract()
            loader.add_value("TitleWiki", title )
            j=j+5

        item = loader.load_item()  # item is loaded with loader data dictionary


        # if "TitleWiki" not in item or "DateWiki" not in item or "UrlWiki" not in item or "DeadlineWiki" not in item or "PlaceWiki" not in item: #you do it
        #     print("item is not loaded properly")
        #     raise ValueError
        if "TitleWiki" not in item :
            raise ValueError("TitleWiki item is not loaded")
        if "DateWiki" not in item :
            raise ValueError("DateWiki item is not loaded")
        if "UrlWiki" not in item :
            raise ValueError("UrlWiki item is not loaded")
        if "DeadlineWiki" not in item :
            raise ValueError("DeadlineWiki item is not loaded")
        if "PlaceWiki" not in item :
            raise ValueError("PlaceWiki item is not loaded")

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
            if item['DateWiki'][k]=="N/A" or item['DateWiki'][k]=="TBD" or item["DateWiki"][k]=="Online" or item["DateWiki"][k]=="ONLINE":
                mydict["date"].append(None)
                #mydict["date"].append(item['DateWiki'][k].split("-")[0][0:12].rstrip())
            else:
                mydict["date"].append(datetime.strptime(item['DateWiki'][k].split("-")[0][0:12].rstrip(),'%b %d, %Y'))

            mydict["url"].append('http://www.wikicfp.com' + item["UrlWiki"][k])
            mydict["paperType"].append("Wiki")
            mydict["where"].append(item["PlaceWiki"][k])

            if item["DeadlineWiki"][k]=="TBD" or item["DeadlineWiki"][k]=="N/A" :#TBD
                mydict["deadline"].append(None)
            elif (len(item["DeadlineWiki"][k])>=12): #with brackets
                mydict["deadline"].append(datetime.strptime(item['DeadlineWiki'][k].split("(")[0][0:12].rstrip(), '%b %d, %Y'))

            else: # normal case
                mydict["deadline"].append(datetime.strptime(item['DeadlineWiki'][k],'%b %d, %Y'))


        #Calling pipeline
        myPipeline = ScrapyProjectPipeline()
        myPipeline.process_item(mydict, SpiderWiki)
        yield mydict#calling pipelines 1 time




def sum(x, y):
    return x + y
def sum1(x,y):
    mydict="what is this"
    return(mydict)
def valuePlusOne(x):
    return x+1