# Generated by Django 3.2.2 on 2021-05-11 06:55

from django.conf import settings
from django.db import migrations
from django.utils.translation import pgettext

from pretix.base.i18n import language
from pretix.base.settings import PERSON_NAME_SALUTATIONS


def normalize_salutations(apps, schema_editor):
    models = (
        ("pretixbase", "Customer", "name_parts"),
        ("pretixbase", "InvoiceAddress", "name_parts"),
        ("pretixbase", "Membership", "attendee_name_parts"),
        ("pretixbase", "CartPosition", "attendee_name_parts"),
        ("pretixbase", "OrderPosition", "attendee_name_parts"),
        ("pretix_exhibitors", "Exhibitor", "contact_name_parts"),
    )

    for salutation, value in PERSON_NAME_SALUTATIONS:
        salutations = []
        for lang in settings.LANGUAGES:
            with language(lang[0]):
                salutation_localized = pgettext("person_name_salutation", salutation)
                if (
                    salutation_localized != salutation
                    and salutation_localized not in salutations
                ):
                    salutations.append(salutation_localized)

        for app, model, key in models:
            sort_params = {}
            sort_params["{}__salutation__in".format(key)] = salutations
            try:
                m = apps.get_model(app, model)
            except LookupError:
                continue
            try:
                qs = m.objects
            except AttributeError:
                qs = m.all

            for o in qs.filter(**sort_params):
                val = getattr(o, key)
                val["salutation"] = salutation
                setattr(o, key, val)
                o.save()


class Migration(migrations.Migration):

    dependencies = [
        ("pretixbase", "0186_invoice_sent_to_organizer"),
    ]

    operations = [
        migrations.RunPython(
            normalize_salutations,
            migrations.RunPython.noop,
        ),
    ]
