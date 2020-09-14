
from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.http import TextResponse

from scrapy_project.scrapy_project.spiders.Spiders import SpiderBmbf,SpiderWiki

#from scrapy_project.scrapy_project.pipelines import ScrapyProjectPipeline #will be delete
class Command(BaseCommand):
    help = "test the spiders"

    def handle(self, *args, **options):
        myTest=Test_ex11()
        myTest.test_Bmbf_parse_has_yield()
        myTest.test_Wiki_parse_has_yield()
        myTest.test_Bmbf_proper_items_yielded()
        #myTest.test_Wiki_proper_items_yielded()
        myTest.test_Bmbf_Xpath_change()

import requests
import types
import unittest
from unittest import mock
from unittest.mock import patch
from scrapy.http import Request

class Test_ex11(unittest.TestCase):

    def test_Bmbf_parse_has_yield(self):
        testSpider=SpiderBmbf()
        testSpider.start_urls=['https://www.bmbf.de/foerderungen/']
        Mydict=testSpider.parse(Request('https://www.bmbf.de/foerderungen/'))
        self.assertIsInstance(Mydict,types.GeneratorType)

    def test_Wiki_parse_has_yield(self):
        testSpider=SpiderWiki()
        testSpider.start_urls=['http://www.wikicfp.com/cfp/']
        Mydict=testSpider.parse(Request('http://www.wikicfp.com/cfp/'))
        self.assertIsInstance(Mydict,types.GeneratorType)

    def test_Bmbf_proper_items_yielded(self):
        testSpider=SpiderBmbf()
        url=testSpider.start_urls=['https://www.bmbf.de/foerderungen/']
        response=TextResponse(url='https://www.bmbf.de/foerderungen/', request=Request('https://www.bmbf.de/foerderungen/'))
        Mydict=testSpider.parse(response)
        print(Mydict)
        # for key in Mydict:
        #     print(key)

            # self.assertIn("title",key)
            # self.assertIn("date",key)
            # self.assertIn("url", key)
            # self.assertIn("paperType", key)
            # self.assertIn("where", key)
            # self.assertIn("deadline", key)

    def test_Wiki_proper_items_yielded(self):
        testSpider = SpiderWiki()
        response = Request('http://www.wikicfp.com/cfp/')
        print(type(Request('http://www.wikicfp.com/cfp/')))
        Mydict = testSpider.parse(response)

        # for key in Mydict:
        #     self.assertIn("title",key)
        #     self.assertIn("date",key)
        #     self.assertIn("url", key)
        #     self.assertIn("paperType", key)
        #     self.assertIn("where", key)
        #     self.assertIn("deadline", key)

        #response is not getting properly
    def test_Bmbf_Xpath_change(self):
        testSpider = SpiderBmbf()
        response = Request('http://www.wikicfp.com/cfp/')
        testSpider.TitleXpath= '//article[@class="block-teaser block-teaser--noimage"][@role="article"]/div[@class="teaser-conten"]//h3/text()'
        Mydict = testSpider.parse(response)
        print(testSpider.TitleXpath)

