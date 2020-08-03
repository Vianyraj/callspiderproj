from __future__ import unicode_literals

from django.db import models


# Create your models here.
# here

# here
class Paper_model(models.Model):  # using the
    Title = models.CharField(max_length=512)
    Dates = models.CharField(max_length=256,null='True')
    Url = models.CharField(max_length=1024)
    PaperType=models.CharField(max_length=64, null='True')
    Where = models.CharField(max_length=256,null='True')
    Deadline = models.CharField(max_length=256,null='True')




