# Generated by Django 3.2.6 on 2021-09-20 11:48

from django.db import migrations, models
import news.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_like_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceid',
            name='name',
            field=models.CharField(default=news.models.name_random, max_length=30, unique=True),
        ),
    ]
