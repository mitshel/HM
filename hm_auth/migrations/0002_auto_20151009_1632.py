# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hm_auth', '0001_squashed_0005_auto_20151003_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='uid',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
