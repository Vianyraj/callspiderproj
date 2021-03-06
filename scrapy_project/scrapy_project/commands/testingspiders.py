#
# from django.core.management.base import BaseCommand
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
# from scrapy.http import TextResponse
#
# #from scrapy_project.scrapy_project.spiders.Spiders import SpiderBmbf,SpiderWiki
# from scrapy_django.questions.models import  Bmbf_model, Wiki_model
# #from scrapy_project.scrapy_project.pipelines import ScrapyProjectPipeline #will be delete
# # class Command(BaseCommand):
# #     help = "test the spiders"
# #
# #     def handle(self, *args, **options):
# #         myTest=Test_ex11()
# #         myTest.test_Bmbf_parse_has_yield()
# #         myTest.test_Wiki_parse_has_yield()
# #         myTest.test_Bmbf_proper_items_yielded()
# #         myTest.test_Bmbf_Path()
# #         myTest.test_Wiki_Path()
# #         #myTest.test_Wiki_proper_items_yielded()
# #         myTest.test_Bmbf_Xpath_change()
# #
# import requests
# import types
# import unittest
# from unittest import mock
# from unittest.mock import patch
# from scrapy.http import Request
# from unittest import TestCase
#
#
#
#
# class TestSum(TestCase):
#
#         def test_sum(self):
#             from scrapy_django.scrapy_project.scrapy_project.spiders.Spiders import sum
#
#             # first store the expected result in a variable
#             result = sum(4, 4)
#
#             # check if the result is equal to expected result
#             # here the result should be equal to 7.
#             self.assertEquals(8, result)


import unittest
from scrapy_django.scrapy_project.scrapy_project.spiders.Spiders import sum,sum1,valuePlusOne
from scrapy_django.questions.models import  Bmbf_model, Wiki_model
from scrapy_django.scrapy_project.scrapy_project.spiders.Spiders import SpiderBmbf,SpiderWiki

from scrapy.http import Request
class Tests(unittest.TestCase):

    def test(self):
        self.assertEqual( valuePlusOne(2), 3)
        print("sssssss")

    def test_neg(self):
        testSpider = SpiderWiki()
        response = Request('http://www.wikicfp.com/cfp/')
        if response:
            Mydict = testSpider.parse(response)
            print("herre",Mydict)
        else:
            print("nonon")
        Mydict = testSpider.parse(response)
        print("myyyy",Mydict)

if __name__ == '__main__':
    unittest.main()