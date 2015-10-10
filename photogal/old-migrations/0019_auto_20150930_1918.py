# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogal', '0018_auto_20150930_1915'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photoalbums',
            options={'ordering': ['title'], 'verbose_name_plural': 'Photo Albums', 'permissions': (('can_view_album', 'Can view album'), ('close_view_album', 'forbidden album view'))},
        ),
    ]
