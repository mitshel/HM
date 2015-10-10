# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [('photogal', '0001_initial'), ('photogal', '0002_auto_20150920_1601'), ('photogal', '0003_setting_description'), ('photogal', '0004_auto_20150920_1603'), ('photogal', '0005_auto_20150920_1607'), ('photogal', '0006_auto_20150920_1849'), ('photogal', '0007_photocat'), ('photogal', '0008_auto_20150921_1921'), ('photogal', '0009_photoimages_cat'), ('photogal', '0010_photocat_album'), ('photogal', '0011_auto_20150921_1958'), ('photogal', '0012_auto_20150921_2001'), ('photogal', '0013_auto_20150921_2019'), ('photogal', '0014_auto_20150921_2033'), ('photogal', '0015_photoimages_thumbnail'), ('photogal', '0016_auto_20150925_2011'), ('photogal', '0017_photoimages_rotateinfo'), ('photogal', '0018_auto_20150930_1915'), ('photogal', '0019_auto_20150930_1918'), ('photogal', '0020_auto_20150930_1919'), ('photogal', '0021_auto_20150930_1929'), ('photogal', '0022_auto_20150930_1936'), ('photogal', '0023_photocollections')]

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('value', models.CharField(blank=True, max_length=256)),
                ('description', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoAlbums',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('base_path', models.CharField(max_length=1024)),
                ('tag', models.CharField(blank=True, max_length=16)),
            ],
            options={
                'verbose_name_plural': 'Photo Albums',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='PhotoImages',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('path', models.CharField(max_length=256)),
                ('filename', models.CharField(max_length=256)),
                ('image_date', models.DateField()),
                ('PhotoAlbum', models.ForeignKey(to='photogal.PhotoAlbums')),
                ('cat', models.ForeignKey(null=True, to='photogal.PhotoCat')),
            ],
            options={
                'verbose_name_plural': 'Photo Images',
                'ordering': ['PhotoAlbum', 'path', 'title'],
            },
        ),
        migrations.AlterField(
            model_name='photoalbums',
            name='base_path',
            field=models.CharField(max_length=1024, default='X:\\MY_DOCS\\DOCUMS\\Foto\\_ФОТОАРХИВ'),
        ),
        migrations.AlterField(
            model_name='photoalbums',
            name='tag',
            field=models.CharField(unique=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='photoalbums',
            name='base_path',
            field=models.CharField(max_length=256, default='X:\\MY_DOCS\\DOCUMS\\Foto\\_ФОТОАРХИВ'),
        ),
        migrations.AlterModelOptions(
            name='photoimages',
            options={'verbose_name_plural': 'Photo Images', 'ordering': ['album', 'path', 'title']},
        ),
        migrations.RenameField(
            model_name='photoimages',
            old_name='PhotoAlbum',
            new_name='album',
        ),
        migrations.CreateModel(
            name='PhotoCats',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('path', models.CharField(blank=True, max_length=256)),
                ('type', models.IntegerField(default=0)),
                ('album', models.ForeignKey(null=True, to='photogal.PhotoAlbums')),
                ('parent', models.ForeignKey(null=True, to='photogal.PhotoCats')),
            ],
            options={
                'verbose_name_plural': 'Photo Catalogs',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='photoimages',
            name='cat',
            field=models.ForeignKey(null=True, to='photogal.PhotoCats'),
        ),
        migrations.AddField(
            model_name='photoimages',
            name='errorflag',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='photoimages',
            name='rotateinfo',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterModelOptions(
            name='photoalbums',
            options={'permissions': (('can_view_album', 'Can view album'),), 'verbose_name_plural': 'Photo Albums', 'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='photoalbums',
            options={'permissions': (('can_view_album', 'Can view album'), ('close_view_album', 'forbidden album view')), 'verbose_name_plural': 'Photo Albums', 'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='photoalbums',
            options={'permissions': (('can_view_album', 'Can view album'),), 'verbose_name_plural': 'Photo Albums', 'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='photoalbums',
            name='allow_group',
            field=models.ForeignKey(blank=True, to='auth.Group', null=True, related_name='allow_group'),
        ),
        migrations.AddField(
            model_name='photoalbums',
            name='deny_group',
            field=models.ForeignKey(blank=True, to='auth.Group', null=True, related_name='deny_group'),
        ),
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
