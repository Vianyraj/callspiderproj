# Generated by Django 3.0.6 on 2020-09-07 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0010_auto_20200907_2203'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Wiki_model',
        ),
        migrations.AlterField(
            model_name='paper_model',
            name='Dates',
            field=models.DateField(null='True'),
        ),
        migrations.AlterField(
            model_name='paper_model',
            name='Deadline',
            field=models.DateField(null='True'),
        ),
    ]
