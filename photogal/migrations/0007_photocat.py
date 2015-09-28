# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogal', '0006_auto_20150920_1849'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoCat',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('path', models.CharField(blank=True, max_length=256)),
                ('type', models.IntegerField(default=0)),
                ('parent', models.ForeignKey(to='photogal.PhotoCat')),
            ],
            options={
                'verbose_name_plural': 'Photo Catalogs',
                'ordering': ['name'],
            },
        ),
    ]
