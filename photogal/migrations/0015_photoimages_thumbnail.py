# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogal', '0014_auto_20150921_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoimages',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='thumbs'),
        ),
    ]
