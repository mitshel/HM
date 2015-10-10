# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hm_auth', '0002_auto_20151003_1602'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HMUser',
            new_name='User',
        ),
    ]
