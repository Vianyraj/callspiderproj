
from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scrapy_project.scrapy_project.spiders.Spiders import SpiderBmbf,SpiderWiki

#from scrapy_project.scrapy_project.pipelines import ScrapyProjectPipeline #will be delete
class Command(BaseCommand):
    help = "Release the spiders"
    # temp=ScrapyProjectPipeline()
    # temp.process_item({"title":"abc"},SpiderBmbf)


    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())

        process.crawl(SpiderBmbf)
        #process.crawl(SpiderWiki)
        process.start()