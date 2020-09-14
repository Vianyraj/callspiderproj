import time
from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy_project.scrapy_project.spiders.Spiders import SpiderBmbf,SpiderWiki

#from scrapy_project.scrapy_project.pipelines import ScrapyProjectPipeline #will be delete
class Command(BaseCommand):
    help = "test the runtime of the spiders"

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())
        t0 = time.time()
        for i in range(10):

            #process.crawl(SpiderBmbf)
            process.crawl(SpiderWiki) #for wiki
        process.start()
        t1 = time.time()
        print("runtime of SpiderWiki", t1-t0)
        print("Pipeline for Wiki called once")



