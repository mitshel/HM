# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogal', '0001_squashed_0023_photocollections'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photocollections',
            options={'verbose_name_plural': 'Photo Collections', 'ordering': ['-favorite', 'title']},
        ),
    ]
