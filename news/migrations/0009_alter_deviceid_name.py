# Generated by Django 3.2.6 on 2021-09-20 11:54

from django.db import migrations, models
import news.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_alter_deviceid_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceid',
            name='name',
            field=models.CharField(max_length=30, verbose_name=news.models.name_random),
        ),
    ]