# Generated by Django 2.2.3 on 2020-05-05 10:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200505_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 5, 10, 0, 26, 149411, tzinfo=utc), verbose_name='创建时间'),
        ),
    ]