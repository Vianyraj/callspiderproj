# # # -*- coding: utf-8 -*-
# # """
# # Created on 2017年11月8日
# # @author: Leo
#
#
# from scrapy.commands import ScrapyCommand
# from scrapy.utils.project import get_project_settings
# from scrapy.crawler import CrawlerProcess
#
# import sys
# sys.path.insert(0, 'C:\\Users\\Vinay\\PycharmProjects\\callspiderproj')
# from scrapy_django.scrapy_project.scrapy_project.spiders.stackoverflow import Bmbf_spiders, WikiSpider
#
#
# class Command(ScrapyCommand):
#     requires_project = True
#
#     def syntax(self):
#         return '[options]'
#
#     def short_desc(self):
#         return 'Runs all of the spiders'
#
#     def add_options(self, parser):
#         ScrapyCommand.add_options(self, parser)
#
#     def process_options(self, args, opts):
#         ScrapyCommand.process_options(self, args, opts)
#
#     def run(self, args, opts):
#         settings = get_project_settings()
#         one = Bmbf_spiders()
#         two = WikiSpider()
#         process = CrawlerProcess(settings)
#         process.crawl(Bmbf_spiders)
#
#         process.crawl(WikiSpider)
#         process.start()
# import scrapy
# from scrapy.crawler import CrawlerProcess
# from scrapy_project.spiders.Spiders import SpiderBmbf,SpiderWiki
# from scrapy_django.scrapy_project.scrapy_project.pipelines import ScrapyProjectPipeline
# class MySpider1(scrapy.Spider):
#     name="MySpider1"
#     # Your first spider definition
#     print("1111111111111111111111111111111111111")
#     start_urls = ['http://www.wikicfp.com/cfp/']
#     def parse(self, response):
#         print("1111111111111111111111111111111111111")
#
#         yield { "title" : "12345" }
#
#
# class MySpider2(scrapy.Spider):
#     name="MySpider2"
#
#     print("222222222222222222222222222222222222222")
#
# process = CrawlerProcess()
# process.crawl(SpiderBmbf)
# process.crawl(MySpider1)
#
#
# process.start() # the script will block here until all crawling jobs are finished
# # temp = ScrapyProjectPipeline.process_item()
# # temp.parse_data({ "title" : "12345" },MySpider1)