# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoAlbums',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=64)),
                ('base_path', models.CharField(max_length=1024)),
                ('tag', models.CharField(max_length=16, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Photo Albums',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='PhotoImages',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=256)),
                ('path', models.CharField(max_length=1024)),
                ('filename', models.CharField(max_length=256)),
                ('image_date', models.DateField()),
                ('PhotoAlbum', models.ForeignKey(to='photogal.PhotoAlbums')),
            ],
            options={
                'verbose_name_plural': 'Photo Images',
                'ordering': ['PhotoAlbum', 'path', 'title'],
            },
        ),
        migrations.AlterField(
            model_name='setting',
            name='value',
            field=models.CharField(max_length=1024, blank=True),
        ),
    ]
