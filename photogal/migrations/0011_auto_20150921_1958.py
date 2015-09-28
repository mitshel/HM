# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photogal', '0010_photocat_album'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photoimages',
            options={'verbose_name_plural': 'Photo Images', 'ordering': ['album', 'path', 'title']},
        ),
        migrations.RenameField(
            model_name='photoimages',
            old_name='PhotoAlbum',
            new_name='album',
        ),
    ]
