# Generated by Django 3.2.6 on 2021-09-17 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceid',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
