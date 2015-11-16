# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogal', '0002_auto_20151010_1505'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photocats',
            options={'ordering': ['-name'], 'verbose_name_plural': 'Photo Catalogs'},
        ),
        migrations.AddField(
            model_name='photocollections',
            name='access_hash',
            field=models.CharField(null=True, blank=True, max_length=32),
        ),
        migrations.AddField(
            model_name='photocollections',
            name='guest_access',
            field=models.BooleanField(default=False),
        ),
    ]
