# Generated by Django 2.0.3 on 2018-03-27 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0014_auto_20180327_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
