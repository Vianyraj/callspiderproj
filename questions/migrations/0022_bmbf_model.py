# Generated by Django 3.0.6 on 2020-09-15 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0021_delete_bmbf_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bmbf_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=1024)),
                ('Dates', models.DateTimeField(null='True')),
                ('Url', models.CharField(max_length=1024)),
                ('Deadline', models.DateTimeField(null='True')),
            ],
        ),
    ]
