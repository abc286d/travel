# Generated by Django 2.0.3 on 2018-03-19 08:35

import ckeditor.fields
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20180319_0423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='activity',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 19, 8, 35, 2, 550957, tzinfo=utc)),
        ),
    ]