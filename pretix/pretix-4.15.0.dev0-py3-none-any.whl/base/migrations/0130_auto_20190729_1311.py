# Generated by Django 2.2.1 on 2019-07-29 13:11

import django.db.models.deletion
from django.db import migrations, models

import pretix.base.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0129_auto_20190724_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='row_name',
            field=models.CharField(default='', max_length=190),
        ),
        migrations.AddField(
            model_name='seat',
            name='seat_number',
            field=models.CharField(default='', max_length=190),
        ),
        migrations.AddField(
            model_name='seat',
            name='zone_name',
            field=models.CharField(default='', max_length=190),
        ),
    ]
