# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from photogal.models import Setting, PhotoAlbums, PhotoImages
from django.utils import timezone
import os

class Command(BaseCommand):
    help = 'List Existing PhotoAlbums.'

    def add_arguments(self, parser):
        parser.add_argument('--verbose',action='store_true', dest='verbose', default=False, help='Set verbosity level for List output.')

    def handle(self, *args, **options):
        for album in PhotoAlbums.objects.all():
            if options['verbose']:
                self.stdout.write('"%s" "%s" %s'%(album.tag, album.title, album.base_path))
            else:
                self.stdout.write('%s'%album.tag)

