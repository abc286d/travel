# Generated by Django 2.0.3 on 2018-03-30 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0016_auto_20180330_2224'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ('-updated',)},
        ),
        migrations.RemoveField(
            model_name='activity',
            name='url',
        ),
        migrations.AlterField(
            model_name='activity',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='活动主图'),
        ),
    ]
