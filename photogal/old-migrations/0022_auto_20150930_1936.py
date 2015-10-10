# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogal', '0021_auto_20150930_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoalbums',
            name='allow_group',
            field=models.ForeignKey(related_name='allow_group', null=True, blank=True, to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='photoalbums',
            name='deny_group',
            field=models.ForeignKey(related_name='deny_group', null=True, blank=True, to='auth.Group'),
        ),
    ]
