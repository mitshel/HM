# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from photogal.models import Setting, PhotoAlbums, PhotoImages, PhotoCats
from photogal.models import PHOTOGAL_THUMBS_ROOT
import os
import shutil

class Command(BaseCommand):
    help = 'Clear PhotoAlbum by tag.'

    def add_arguments(self, parser):
        parser.add_argument('album_tags',nargs='+', help='List of unique tags of PhotoAlbums.')

    def handle(self, *args, **options):
        self.stdout.write('Startup photoclear function.')
        for tag_name in options['album_tags']:
            try:
                album=PhotoAlbums.objects.get(tag=tag_name)
            except PhotoAlbums.DoesNotExist:
                self.stdout.write('Not find PhotoAlbum for tag:"%s"'%tag_name)
            else:
                self.stdout.write('Deleting all images from album "%s" for tagname:"%s". Album path: %s.'%(album.title,tag_name, album.base_path))
                album_images=PhotoImages.objects.filter(album=album)
                album_images.delete()

                album_cats=PhotoCats.objects.filter(album=album)
                album_cats.delete()
                cat=os.path.join(PHOTOGAL_THUMBS_ROOT, album.tag)
                if os.path.exists(cat):
                    shutil.rmtree(cat)



