# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from photogal.models import Setting, PhotoAlbums, PhotoImages, addimage
from django.utils import timezone
import os

class Command(BaseCommand):
    help = 'Scan PhotoAlbum by tag.'

    def add_arguments(self, parser):
        parser.add_argument('album_tags',nargs='*', help='List of unique tags of PhotoAlbums.')
        parser.add_argument('--all',action='store_true', dest='all', default=False, help='Scan all existing albums.')
        parser.add_argument('--verbose',action='store_true', dest='verbose', default=False, help='Set verbosity level for photoimages scan.')

    def handle(self, *args, **options):
        self.stdout.write('Startup photoscan function.')
        if options['all']:
            self.scan_all(options['verbose'])
        else:
            for tag_name in options['album_tags']:
                try:
                    album=PhotoAlbums.objects.get(tag=tag_name)
                except PhotoAlbums.DoesNotExist:
                    self.stdout.write('Not find PhotoAlbum for tag:"%s"'%tag_name)
                else:
                    self.scan_album(album, options['verbose'])

    def scan_album(self,album,verbose=False):
        self.stdout.write('Scanning album "%s" for tagname:"%s". Album base path: %s.'%(album.title,album.tag,album.base_path))
        VALID_EXT=Setting.objects.get(name='valid_ext').value.split()
        BASE_PATH=album.base_path
        for full_path, dirs, files in os.walk(album.base_path, followlinks=True):
            for name in files:
                (n,e)=os.path.splitext(name)
                if e.lower() in VALID_EXT:
                    rel_path=os.path.relpath(full_path,BASE_PATH)
                    if verbose:
                        self.stdout.write('Adding file %s in relative path %s'%(name, rel_path))
                    img=addimage(name, name, rel_path, album)

    def scan_all(self,verbose=False):
        for a in PhotoAlbums.objects.all():
            self.scan_album(a,verbose)

