# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hm_auth', '0004_auto_20151003_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='select_list',
            field=models.TextField(null=True, blank=True),
        ),
    ]
