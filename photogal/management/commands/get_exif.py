# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from photogal.models import Setting, PhotoAlbums, PhotoImages, PhotoCats
import os
from PIL import Image
from PIL.ExifTags import TAGS

class Command(BaseCommand):
    help = 'Get EXIF info from PHOTO by ID'

    def add_arguments(self, parser):
        parser.add_argument('photo_id',nargs='+', help='List of photo_id', type=int)
        parser.add_argument('--tags',nargs='+',action='store', dest='tags', default='all', help='Get EXIF tags values, listed in lower case.', type=str)
        parser.add_argument('--taglist',action='store_true', dest='taglist', default=False, help='Get all EXIF tags names')

    def handle(self, *args, **options):
        for photo_id in options['photo_id']:
            try:
                img=PhotoImages.objects.get(id=photo_id)
            except PhotoAlbums.DoesNotExist:
                self.stdout.write('Not find PhotoImage for ID:"%s"'%photo_id)
            else:
                self.stdout.write('Get EXIF data (%s) for photo( album:%s, path:%s, filename:%s)'%(options['tags'],img.album.tag, img.path, img.filename))
                full_path=os.path.join(img.album.base_path, img.path, img.filename)
                if os.path.exists(full_path):
                    photo=Image.open(full_path)

                    # Получаем Exif
                    try:
                        exif = photo._getexif()
                    except:
                        exif = None
                        self.stdout.write('Error getting EXIF Data')

                    if exif != None:
                        for tag, value in exif.items():
                            decoded = TAGS.get(tag, tag)
                            if options['taglist']:
                                self.stdout.write('%s'%decoded)
                            else:
                                if isinstance(decoded,str):
                                    if ('all' in options['tags']) or (decoded.lower() in options['tags']) or (decoded in options['tags']):
                                        self.stdout.write('%s = %s'%(decoded,value))
                else:
                    self.stdout.write('Image file not found!')


