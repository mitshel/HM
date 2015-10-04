# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photogal', '0022_auto_20150930_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoCollections',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('photo_list', models.TextField(blank=True, null=True)),
                ('favorite', models.BooleanField(default=False)),
                ('uid', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Photo Collections',
                'ordering': ['title'],
            },
        ),
    ]
