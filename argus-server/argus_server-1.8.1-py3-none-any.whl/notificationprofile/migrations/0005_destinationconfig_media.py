# Generated by Django 3.2.6 on 2022-01-21 13:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
from rest_framework.exceptions import APIException

from argus.notificationprofile.media import MEDIA_CLASSES


def create_default_media(apps, schema_editor):
    Media = apps.get_model("argus_notificationprofile", "Media")
    db_alias = schema_editor.connection.alias
    media = [Media(slug=medium.MEDIA_SLUG, name=medium.MEDIA_NAME) for medium in MEDIA_CLASSES]
    Media.objects.using(db_alias).bulk_create(media)


def create_and_link_default_email_destinations(apps, schema_editor):
    Users = apps.get_model("argus_auth", "User")
    DestinationConfig = apps.get_model("argus_notificationprofile", "DestinationConfig")
    Media = apps.get_model("argus_notificationprofile", "Media")
    db_alias = schema_editor.connection.alias
    email = Media.objects.using(db_alias).get(slug="email")

    for user in Users.objects.exclude(email=""):
        DestinationConfig.objects.using(db_alias).create(
            user=user,
            media=email,
            settings={
                "email_address": user.email,
                "synced": True,
            },
        )


def create_sms_destinations(apps, schema_editor):
    PhoneNumber = apps.get_model("argus_auth", "PhoneNumber")
    DestinationConfig = apps.get_model("argus_notificationprofile", "DestinationConfig")
    Media = apps.get_model("argus_notificationprofile", "Media")
    db_alias = schema_editor.connection.alias

    if PhoneNumber.objects.exists():
        try:
            sms = Media.objects.using(db_alias).get(slug="sms")
        except Media.DoesNotExist:
            raise APIException("SMS plugin is not registered in MEDIA_PLUGINS")

        for phone_number in PhoneNumber.objects.all():
            DestinationConfig.objects.using(db_alias).create(
                user=phone_number.user,
                media=sms,
                settings={
                    "phone_number": str(phone_number.phone_number),
                },
            )


def copy_notificationprofiles_to_destinations(apps, schema_editor):
    DestinationConfig = apps.get_model("argus_notificationprofile", "DestinationConfig")
    Media = apps.get_model("argus_notificationprofile", "Media")
    NotificationProfile = apps.get_model("argus_notificationprofile", "NotificationProfile")
    email = Media.objects.get(slug="email")
    if (
        NotificationProfile.objects.filter(media_v1=["EM", "SM"]).exists()
        or NotificationProfile.objects.filter(media_v1=["SM"]).exists()
    ):
        try:
            sms = Media.objects.get(slug="sms")
        except Media.DoesNotExist:
            raise APIException("SMS plugin is not registered in MEDIA_PLUGINS")

    for profile in NotificationProfile.objects.all():
        if profile.user.email and profile.media_v1 in [["EM", "SM"], ["SM", "EM"], ["EM"]]:
            destination, _ = DestinationConfig.objects.get_or_create(
                user=profile.user,
                media=email,
                settings={
                    "email_address": profile.user.email,
                    "synced": True,
                },
            )
            profile.destinations.add(destination)

        if profile.phone_number and profile.media_v1 in [["EM", "SM"], ["SM", "EM"], ["SM"]]:
            destination, _ = DestinationConfig.objects.get_or_create(
                user=profile.user,
                media=sms,
                settings={
                    "phone_number": str(profile.phone_number.phone_number),
                },
            )
            profile.destinations.add(destination)


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("argus_notificationprofile", "0004_copy_notificationprofile_media_to_media_v1"),
    ]

    operations = [
        migrations.CreateModel(
            name="Media",
            fields=[
                ("slug", models.SlugField(blank=True, max_length=20, primary_key=True)),
                ("name", models.CharField(max_length=20)),
            ],
            options={
                "verbose_name": "Medium",
                "verbose_name_plural": "Media",
            },
        ),
        migrations.CreateModel(
            name="DestinationConfig",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("label", models.CharField(blank=True, max_length=50, null=True)),
                ("settings", models.JSONField()),
                (
                    "media",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="destinations",
                        to="argus_notificationprofile.media",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="destinations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="notificationprofile",
            name="destinations",
            field=models.ManyToManyField(
                blank=True,
                related_name="notification_profile",
                to="argus_notificationprofile.DestinationConfig",
            ),
        ),
        migrations.AddConstraint(
            model_name="destinationconfig",
            constraint=models.UniqueConstraint(fields=("user", "settings"), name="unique_destination_per_user"),
        ),
        migrations.AddConstraint(
            model_name="destinationconfig",
            constraint=models.UniqueConstraint(
                fields=("user", "media", "label"),
                name="unique_label_per_user_and_medium",
            ),
        ),
        migrations.RunPython(create_default_media, migrations.RunPython.noop),
        migrations.RunPython(create_and_link_default_email_destinations, migrations.RunPython.noop),
        migrations.RunPython(create_sms_destinations, migrations.RunPython.noop),
        migrations.RunPython(copy_notificationprofiles_to_destinations, migrations.RunPython.noop),
    ]
