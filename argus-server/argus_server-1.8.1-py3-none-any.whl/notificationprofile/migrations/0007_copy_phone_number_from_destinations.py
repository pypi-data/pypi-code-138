# Generated by Django 3.2.6 on 2022-02-13 17:10

from django.db import migrations
from django.db.models import Q


def copy_destinations_to_media_and_media_v1(apps, schema_editor):
    NotificationProfile = apps.get_model("argus_notificationprofile", "NotificationProfile")

    for profile in NotificationProfile.objects.all():
        if (
            profile.destinations.filter(media_id="email").exists()
            and profile.destinations.filter(media_id="sms").exists()
        ):
            profile.media = ["EM", "SM"]
            profile.media_v1 = ["EM", "SM"]
        elif profile.destinations.filter(media_id="email").exists():
            profile.media = ["EM"]
            profile.media_v1 = ["EM"]
        elif profile.destinations.filter(media_id="sms").exists():
            profile.media = ["SM"]
            profile.media_v1 = ["SM"]
        profile.save(update_fields=["media", "media_v1"])


def link_phone_numbers_with_notification_profiles(apps, schema_editor):
    PhoneNumber = apps.get_model("argus_auth", "PhoneNumber")
    NotificationProfile = apps.get_model("argus_notificationprofile", "NotificationProfile")
    db_alias = schema_editor.connection.alias

    changed_profiles = []
    for profile in NotificationProfile.objects.filter(destinations__media_id="sms"):
        phone_number = profile.destinations.filter(media_id="sms").order_by("pk").first().settings["phone_number"]
        profile.phone_number = PhoneNumber.objects.using(db_alias).get(
            Q(user=profile.user) & Q(phone_number=phone_number)
        )
        changed_profiles.append(profile)
    if changed_profiles:
        NotificationProfile.objects.bulk_update(objs=changed_profiles, fields=["phone_number"])


class Migration(migrations.Migration):

    dependencies = [
        ("argus_notificationprofile", "0006_related_name_destinations"),
    ]

    operations = [
        migrations.RunPython(migrations.RunPython.noop, link_phone_numbers_with_notification_profiles),
        migrations.RunPython(migrations.RunPython.noop, copy_destinations_to_media_and_media_v1),
    ]
