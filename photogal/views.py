# -*- coding: utf-8 -*-

from django.template import Context, RequestContext
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from photogal.models import Setting, PhotoAlbums, PhotoImages, PhotoCats, addthumb
from django.conf import settings
from django.db.models import Q
import os

class breadcumb:
    def __init__(self, title='',href='#' ,cl=None):
        self.href=href
        self.title=title
        self.cl=cl

def photogal_processor(request):
    args={}
    args['app_name']=settings.PHOTOGAL_APP_NAME
    args['app_ver']='0.01'
    user=request.user
    if user.is_authenticated():
        args['albums']=PhotoAlbums.objects.filter(Q(allow_group__in=user.groups.values('id'))&~Q(deny_group__in=user.groups.values('id')))
    return args

# Create your views here.
def hello(request):
    args = RequestContext(request)
    return render_to_response('hello.html', args)



def show_page(request, album_id=None, cat_id=None):
    class element:
        def __init__(self, type=0, id=0, title='', full_path='', thumb_path='', prev_path='', url='', errorflag=0):
            self.type=type         # 0 - Directory, 1 - ImageFile, 2 - VideoFile, -1 - none
            self.title=title
            self.full_path=full_path
            self.thumb_path=thumb_path
            self.prev_path=prev_path
            self.image_url=url
            self.id=id
            self.errorflag=errorflag

    args = RequestContext(request)
    scolumns=Setting.objects.get(name='album_columns').value
    if scolumns.isdigit():
        max_columns=int(scolumns)
    else:
        max_columns=3

    if album_id==None:
        album=PhotoAlbums.objects.first()
    else:
        album=PhotoAlbums.objects.get(id=album_id)

    if cat_id!=None:
        folder=PhotoCats.objects.get(id=cat_id)
    else:
        folder=None

    breadcumbs=[]
    f=folder
    cl='current'
    while f:
        breadcumbs.insert(0,breadcumb(f.name, "/photo/album/%s/%s/"%(album.id,f.id),cl))
        cl=None
        f=f.parent
    breadcumbs.insert(0,breadcumb(album.title,"/photo/album/%s/"%album.id,cl))

    folders=[]
    catalogs=PhotoCats.objects.filter(album=album, parent_id=cat_id)
    for c in catalogs:
        folders.append(element(0, c.id, c.name, c.path))

    photos=[]
    images=PhotoImages.objects.filter(album=album, cat=cat_id)
    for i in images:
        full_path=os.path.join(album.base_path,i.path,i.filename).replace('\\','/')
        thumb_path=os.path.join(settings.PHOTOGAL_THUMBS_DIR,album.tag,i.path,addthumb(i.filename,settings.PHOTOGAL_THUMB_STR)).replace('\\','/')
        prev_path=os.path.join(settings.PHOTOGAL_THUMBS_DIR,album.tag,i.path,addthumb(i.filename, settings.PHOTOGAL_PREV_STR)).replace('\\','/')
        photos.append(element(1, i.id, i.title, full_path, thumb_path, prev_path, i.errorflag))

    args['folders'] = folders
    args['photos'] = photos
    args['album_id'] = album.id
    args['album'] = album
    args['folder'] = folder
    args['breadcumbs'] = breadcumbs

    return render_to_response('album.html', args)