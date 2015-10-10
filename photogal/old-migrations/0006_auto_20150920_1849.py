# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogal', '0005_auto_20150920_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoalbums',
            name='base_path',
            field=models.CharField(max_length=256, default='X:\\MY_DOCS\\DOCUMS\\Foto\\_ФОТОАРХИВ'),
        ),
        migrations.AlterField(
            model_name='photoimages',
            name='path',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='setting',
            name='value',
            field=models.CharField(max_length=256, blank=True),
        ),
    ]
