# Generated by Django 3.0.6 on 2020-09-07 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0012_auto_20200907_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper_model',
            name='Dates',
            field=models.CharField(max_length=1024, null='True'),
        ),
        migrations.AlterField(
            model_name='paper_model',
            name='Deadline',
            field=models.CharField(max_length=1024, null='True'),
        ),
    ]
