# -*- coding: utf-8 -*-

from django.template import Context, RequestContext
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from photogal.models import Setting, PhotoAlbums, PhotoImages, PhotoCats, PhotoCollections, addthumb
from django.conf import settings
from django.db.models import Q
from django.http import HttpResponse
import os

class breadcumb:
    def __init__(self, title='',href='#' ,cl=None):
        self.href=href
        self.title=title
        self.cl=cl

class element:
    def __init__(self, type=0, id=0, title='', full_path='', thumb_path='', prev_path='', url='', errorflag=0, checked=False):
        self.type=type         # 0 - Directory, 1 - ImageFile, 2 - VideoFile, -1 - none
        self.title=title
        self.full_path=full_path
        self.thumb_path=thumb_path
        self.prev_path=prev_path
        self.image_url=url
        self.id=id
        self.errorflag=errorflag
        self.checked=checked

def photogal_processor(request):
    args={}
    args['app_name']=settings.PHOTOGAL_APP_NAME
    args['app_ver']='0.01'
    user=request.user
    if user.is_authenticated():
        args['albums']=PhotoAlbums.objects.filter(Q(allow_group__in=user.groups.values('id'))&~Q(deny_group__in=user.groups.values('id')))
        args['collections']=PhotoCollections.objects.filter(uid=user)
    return args

# Create your views here.
def hello(request):
    args = RequestContext(request)
    return render_to_response('hello.html', args)



def show_album(request, album_id=None, cat_id=None):
    args = RequestContext(request)
    user=request.user

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
    breadcumbs.insert(0,breadcumb('Фотоальбомы',"/photo/album/",))

    folders=[]
    catalogs=PhotoCats.objects.filter(album=album, parent_id=cat_id)
    for c in catalogs:
        folders.append(element(0, c.id, c.name, c.path))

    photos=[]
    images=PhotoImages.objects.filter(album=album, cat=cat_id)
    try:
        favorites = PhotoCollections.objects.get(favorite=True).get_list()
    except PhotoCollections.DoesNotExist:
        favorites = []

    for i in images:
        full_path=os.path.join(album.base_path,i.path,i.filename).replace('\\','/')
        thumb_path=os.path.join(settings.PHOTOGAL_THUMBS_DIR,album.tag,i.path,addthumb(i.filename,settings.PHOTOGAL_THUMB_STR)).replace('\\','/')
        prev_path=os.path.join(settings.PHOTOGAL_THUMBS_DIR,album.tag,i.path,addthumb(i.filename, settings.PHOTOGAL_PREV_STR)).replace('\\','/')
        checked=(str(i.id) in favorites)
        photos.append(element(1, i.id, i.title, full_path, thumb_path, prev_path,'', i.errorflag, checked))

    args['folders'] = folders
    args['photos'] = photos
    args['album_id'] = album.id
    args['album'] = album
    args['folder'] = folder
    args['breadcumbs'] = breadcumbs

    return render_to_response('album.html', args)

def show_collection(request, collection_id=None):
    args = RequestContext(request)
    user = request.user

    if collection_id==None:
        collection = PhotoCollections.objects.get(favorite=True)
    else:
        collection = PhotoCollections.objects.get(id=collection_id)

    breadcumbs=[]
    cl='current'
    breadcumbs.insert(0,breadcumb(collection.title,"/photo/collect/%s/"%collection.id,cl))
    breadcumbs.insert(0,breadcumb('Коллекции',"/photo/collect/",))

    photos=[]
    images=PhotoImages.objects.filter(Q(id__in = collection.get_list()))

    for i in images:
        full_path=os.path.join(i.album.base_path,i.path,i.filename).replace('\\','/')
        thumb_path=os.path.join(settings.PHOTOGAL_THUMBS_DIR,i.album.tag,i.path,addthumb(i.filename,settings.PHOTOGAL_THUMB_STR)).replace('\\','/')
        prev_path=os.path.join(settings.PHOTOGAL_THUMBS_DIR,i.album.tag,i.path,addthumb(i.filename, settings.PHOTOGAL_PREV_STR)).replace('\\','/')
        photos.append(element(1, i.id, i.title, full_path, thumb_path, prev_path,'', i.errorflag, True))

    args['photos'] = photos
    args['collection'] = collection
    args['breadcumbs'] = breadcumbs

    return render_to_response('album.html', args)

def updateselect(request, id=None, value=0):
    user=request.user
    response = HttpResponse()
    response['Content-Type']="text/javascript"
    result=None
    if isinstance(id,int): id=str(id)
    if isinstance(value,str): value=int(value)
    try:
        favorites = PhotoCollections.objects.get(Q(uid=user)&Q(favorite=True))
    except PhotoCollections.DoesNotExist:
        favorites = PhotoCollections.objects.create(uid=user, favorite=True, photo_list=None, title="Избранное")
    if user.is_authenticated():
        if id!=None:
            if value==1:
                result = favorites.add_photo(id)
                #result=user.userprofile.add_selected(id)
            elif value==0:
                result = favorites.del_photo(id)
                #result=user.userprofile.del_selected(id)

    response.write("{user:%s,id:%s,value:%s,result:%s}"%(user.username,id,value,result))
    return response
