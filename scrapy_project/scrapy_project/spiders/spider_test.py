from ..spiders.Spiders import SpiderBmbf,SpiderWiki
#from scrapy_django.scrapy_project.scrapy_project.spiders.Spiders import SpiderBmbf,SpiderWiki

import requests
import types
import unittest
from unittest import mock
from unittest.mock import patch
from scrapy.http import Request

class Test_ex11(unittest.TestCase):

    def test_Bmbf_parse_has_yield(self):
        testSpiderBmbf=SpiderBmbf()
        print(testSpiderBmbf.start_urls)
        responseBmbf = requests.get('https://www.bmbf.de/foerderungen/')
        MydictBmbf=testSpiderBmbf.parse(responseBmbf)
        self.assertIsInstance(MydictBmbf,types.GeneratorType)

    def test_Wiki_parse_has_yield(self):
        testSpiderWiki=SpiderWiki()
        responseWiki = requests.get('http://www.wikicfp.com/cfp/')
        MydictWiki=testSpiderWiki.parse(responseWiki)
        self.assertIsInstance(MydictWiki,types.GeneratorType)

    def test_Bmbf_proper_items_yielded(self):
        testSpider=SpiderBmbf()
        response = requests.get('https://www.bmbf.de/foerderungen/')
        Mydict=testSpider.parse(response)

        for key in Mydict:
            self.assertIn("title",key)
            self.assertIn("date",key)
            self.assertIn("url", key)
            self.assertIn("paperType", key)
            self.assertIn("where", key)
            self.assertIn("deadline", key)

            #you do it
    def test_Wiki_proper_items_yielded(self):
        testSpider = SpiderWiki()
        response = Request('http://www.wikicfp.com/cfp/')
        print(type(Request('http://www.wikicfp.com/cfp/')))
        Mydict = testSpider.parse(response)

        for key in Mydict:
            self.assertIn("title",key)
            self.assertIn("date",key)
            self.assertIn("url", key)
            self.assertIn("paperType", key)
            self.assertIn("where", key)
            self.assertIn("deadline", key)
        # you do it
        #response is not getting properly


