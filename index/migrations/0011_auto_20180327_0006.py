# Generated by Django 2.0.3 on 2018-03-26 16:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_auto_20180326_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 26, 16, 6, 13, 898535, tzinfo=utc)),
        ),
    ]