# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogal', '0016_auto_20150925_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoimages',
            name='rotateinfo',
            field=models.IntegerField(default=0),
        ),
    ]
