# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogal', '0015_photoimages_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photoimages',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='photoimages',
            name='errorflag',
            field=models.IntegerField(default=0),
        ),
    ]
