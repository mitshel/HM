# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogal', '0011_auto_20150921_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoCats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('path', models.CharField(blank=True, max_length=256)),
                ('type', models.IntegerField(default=0)),
                ('album', models.ForeignKey(to='photogal.PhotoAlbums', null=True)),
                ('parent', models.OneToOneField(null=True, to='photogal.PhotoCats')),
            ],
            options={
                'verbose_name_plural': 'Photo Catalogs',
                'ordering': ['name'],
            },
        ),
        migrations.RemoveField(
            model_name='photocat',
            name='album',
        ),
        migrations.RemoveField(
            model_name='photocat',
            name='parent',
        ),
        migrations.AlterField(
            model_name='photoimages',
            name='cat',
            field=models.ForeignKey(to='photogal.PhotoCats', null=True),
        ),
        migrations.DeleteModel(
            name='PhotoCat',
        ),
    ]
