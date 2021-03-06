# Generated by Django 2.2.3 on 2020-05-05 13:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200505_1829'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_time'], 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 5, 13, 31, 35, 792681, tzinfo=utc), verbose_name='创建时间'),
        ),
    ]
