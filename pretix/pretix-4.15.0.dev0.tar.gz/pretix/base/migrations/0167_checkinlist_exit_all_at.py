# Generated by Django 3.0.10 on 2020-10-20 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0166_auto_20201015_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkinlist',
            name='exit_all_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
