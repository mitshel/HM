# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import Group

from django.db import models, migrations

def create_std_groups(apps, schema_editor):
    Group.objects.create(name='any_album_allow_group')
    Group.objects.create(name='admin_group')

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
         migrations.RunPython(create_std_groups),
    ]
