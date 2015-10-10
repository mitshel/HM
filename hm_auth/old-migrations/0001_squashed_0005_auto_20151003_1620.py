# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [('hm_auth', '0001_initial'), ('hm_auth', '0002_auto_20151003_1602'), ('hm_auth', '0003_auto_20151003_1605'), ('hm_auth', '0004_auto_20151003_1614'), ('hm_auth', '0005_auto_20151003_1620')]

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('select_list', models.TextField(blank=True, null=True)),
                ('uid', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User profiles',
            },
        ),
    ]
