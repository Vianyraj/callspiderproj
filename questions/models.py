



from django.db import models

# Create your models here.

class Wiki_model(models.Model):#call for papers
    Title = models.CharField(max_length=1024)
    Dates = models.DateTimeField(null='True')
    Url = models.CharField(max_length=1024)
    PaperType=models.CharField(max_length=64, null='True')
    Where = models.CharField(max_length=256,null='True')
    Deadline =models.DateTimeField(null='True')
    class Meta:
        db_table="questions_wiki_model"

class Bmbf_model(models.Model):
    Title = models.CharField(max_length=1024)
    Dates = models.DateTimeField(null='True')
    Url = models.CharField(max_length=1024)
    Deadline =models.DateTimeField(null='True')
