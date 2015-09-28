# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogal', '0002_auto_20150920_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='description',
            field=models.CharField(max_length=256, blank=True),
        ),
    ]
