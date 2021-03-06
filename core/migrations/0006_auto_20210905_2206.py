# Generated by Django 3.2.6 on 2021-09-05 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210902_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricedata',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='pricedata',
            name='youtube_id',
        ),
        migrations.CreateModel(
            name='YardData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yard', models.IntegerField()),
                ('youtube_id', models.CharField(max_length=20)),
                ('timestamp', models.DateField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('buy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buy', to='core.pricedata')),
                ('sell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sell', to='core.pricedata')),
            ],
        ),
    ]
