# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogal', '0003_setting_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoalbums',
            name='base_path',
            field=models.CharField(max_length=1024, default='X:\\MY_DOCS\\DOCUMS\\Foto\\_ФОТОАРХИВ'),
        ),
    ]
