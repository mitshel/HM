# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogal', '0019_auto_20150930_1918'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photoalbums',
            options={'permissions': (('can_view_album', 'Can view album'),), 'ordering': ['title'], 'verbose_name_plural': 'Photo Albums'},
        ),
    ]
