# Generated by Django 2.0.3 on 2018-03-26 08:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20180326_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 26, 8, 0, 23, 260135, tzinfo=utc)),
        ),
    ]