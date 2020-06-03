from django.db import models

# Create your models here.

# class paperscrapying(models.Model):
#     id = models.AutoField(primary_key=True)
#     eventlink = models.CharField(max_length=200)
#     eventname = models.CharField(max_length=500)
#     dates = models.CharField(max_length=300)
#     wheree= models.CharField(max_length=300)
#     whene = models.CharField(max_length=400)




class TheodoTeam(models.Model):
        name = models.CharField(max_length=150)
        image = models.CharField(max_length=150)
        fun_fact = models.TextField(blank=True)
        class Meta:
            verbose_name = "theodo UK team"
