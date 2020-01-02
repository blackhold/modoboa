# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-10 15:46
from django.db import migrations


def update_ldap_secured(apps, schema_editor):
    """Update ldap_secured settings."""
    LocalConfig = apps.get_model("core", "LocalConfig")
    lc = LocalConfig.objects.first()
    if lc is None or "ldap_secured" not in lc._parameters:
        return
    if lc._parameters["ldap_secured"]:
        lc._parameters["ldap_secured"] = "ssl"
    else:
        lc._parameters["ldap_secured"] = "none"
    lc.save(update_fields=["_parameters"])


def forward(apps, schema_editor):
    """Empty forward method."""
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20170707_1058'),
    ]

    operations = [
        migrations.RunPython(update_ldap_secured, forward),
    ]
