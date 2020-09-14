from __future__ import unicode_literals

from datetime import datetime

from django.db import models


# Create your models here.
class Paper_model(models.Model):
    Title = models.CharField(max_length=1024)
    Dates = models.CharField(max_length=1024,null='True')
    Url = models.CharField(max_length=1024)
    PaperType=models.CharField(max_length=64, null='True')
    Where = models.CharField(max_length=256,null='True')
    Deadline =models.CharField(max_length=1024,null='True')

# class Wiki_model(models.Model):#call for papers
#     Title = models.CharField(max_length=1024)
#     Dates = models.CharField(max_length=256,null='True')
#     Url = models.CharField(max_length=1024)
#     PaperType=models.CharField(max_length=64, null='True')
#     Where = models.CharField(max_length=256,null='True')
#     Deadline = models.CharField(max_length=256,null='True')
#
class Bmbf_model(models.Model):
    Title = models.CharField(max_length=1024)
    Dates = models.CharField(max_length=256,null='True')
    Url = models.CharField(max_length=1024)
    PaperType=models.CharField(max_length=64, null='True')
    Where = models.CharField(max_length=256,null='True')
    Deadline = models.CharField(max_length=256,null='True')

