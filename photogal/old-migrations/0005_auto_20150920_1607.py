# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogal', '0004_auto_20150920_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoalbums',
            name='tag',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
