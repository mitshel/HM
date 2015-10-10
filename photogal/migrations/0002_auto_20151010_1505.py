# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def photogal_settings(apps, schema_editor):
    setting = apps.get_model("photogal","Setting")
    setting.objects.create(name='base_path', value='', description='Base path to scanned photo collections')
    setting.objects.create(name='valid_ext', value='.jpg .jpeg .png', description='Photofiles extensions')

class Migration(migrations.Migration):

    dependencies = [
        ('photogal', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(photogal_settings),
    ]
