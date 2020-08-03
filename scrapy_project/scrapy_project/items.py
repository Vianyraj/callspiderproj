
import scrapy


class EventItemBmbf(scrapy.Item):#items for BMBF
    TitleBMBF = scrapy.Field()
    DatesBMBF =scrapy.Field()
    UrlBMBF = scrapy.Field()

class EventItemWiki(scrapy.Item):#Items for Wiki
    Titlewiki =scrapy.Field()
    Urlwiki = scrapy.Field()
