# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogal', '0008_auto_20150921_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoimages',
            name='cat',
            field=models.ForeignKey(null=True, to='photogal.PhotoCat'),
        ),
    ]
