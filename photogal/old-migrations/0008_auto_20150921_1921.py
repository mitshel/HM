# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogal', '0007_photocat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photocat',
            name='parent',
            field=models.OneToOneField(to='photogal.PhotoCat', null=True),
        ),
    ]
