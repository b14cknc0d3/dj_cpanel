# Generated by Django 3.2.6 on 2021-09-02 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210902_1758'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='broadcast_email',
            options={'verbose_name': 'BroadCast Email to all Subscribers', 'verbose_name_plural': 'BroadCast Email'},
        ),
        migrations.AlterField(
            model_name='subscribers',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
