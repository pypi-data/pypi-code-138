# Generated by Django 3.0.9 on 2020-10-13 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0162_remove_seat_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='security_profile',
            field=models.CharField(default='full', max_length=190, null=True),
        ),
    ]
