# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogal', '0013_auto_20150921_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photocats',
            name='parent',
            field=models.ForeignKey(null=True, to='photogal.PhotoCats'),
        ),
    ]
