# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoAlbums',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('base_path', models.CharField(max_length=256, blank=True)),
                ('tag', models.CharField(max_length=16, unique=True)),
                ('allow_group', models.ForeignKey(to='auth.Group', null=True, related_name='allow_group', blank=True)),
                ('deny_group', models.ForeignKey(to='auth.Group', null=True, related_name='deny_group', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Photo Albums',
                'permissions': (('can_view_album', 'Can view album'),),
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='PhotoCats',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('path', models.CharField(max_length=256, blank=True)),
                ('type', models.IntegerField(default=0)),
                ('album', models.ForeignKey(null=True, to='photogal.PhotoAlbums')),
                ('parent', models.ForeignKey(null=True, to='photogal.PhotoCats')),
            ],
            options={
                'verbose_name_plural': 'Photo Catalogs',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PhotoCollections',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('photo_list', models.TextField(null=True, blank=True)),
                ('favorite', models.BooleanField(default=False)),
                ('uid', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Photo Collections',
                'ordering': ['-favorite', 'title'],
            },
        ),
        migrations.CreateModel(
            name='PhotoImages',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('path', models.CharField(max_length=256)),
                ('filename', models.CharField(max_length=256)),
                ('image_date', models.DateField()),
                ('errorflag', models.IntegerField(default=0)),
                ('rotateinfo', models.IntegerField(default=0)),
                ('album', models.ForeignKey(to='photogal.PhotoAlbums')),
                ('cat', models.ForeignKey(null=True, to='photogal.PhotoCats')),
            ],
            options={
                'verbose_name_plural': 'Photo Images',
                'ordering': ['album', 'path', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('value', models.CharField(max_length=256, blank=True)),
                ('description', models.CharField(max_length=256, blank=True)),
            ],
        ),
    ]
