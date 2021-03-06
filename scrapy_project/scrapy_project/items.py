
import scrapy


class EventItemBmbf(scrapy.Item):#items for BMBF
    TitleBMBF = scrapy.Field()
    DateBMBF =scrapy.Field()
    UrlBMBF = scrapy.Field()

class EventItemWiki(scrapy.Item):#Items for Wiki
    TitleWiki =scrapy.Field()
    DateWiki = scrapy.Field()
    PlaceWiki = scrapy.Field()
    DeadlineWiki = scrapy.Field()
    UrlWiki = scrapy.Field()
