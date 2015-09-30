# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('photogal', '0020_auto_20150930_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoalbums',
            name='allow_group',
            field=models.ForeignKey(null=True, related_name='allow_group', to='auth.Group'),
        ),
        migrations.AddField(
            model_name='photoalbums',
            name='deny_group',
            field=models.ForeignKey(null=True, related_name='deny_group', to='auth.Group'),
        ),
    ]
