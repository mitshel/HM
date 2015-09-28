# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
import os
from PIL import Image
from PIL.ExifTags import TAGS
from HM.settings import MEDIA_ROOT, PHOTOGAL_THUMBS_DIR, PHOTOGAL_THUMBS_SIZE, PHOTOGAL_THUMBS_SQUARE, PHOTOGAL_PREVIEW_SIZE, PHOTOGAL_THUMB_STR, PHOTOGAL_PREV_STR

PHOTOGAL_THUMBS_ROOT = os.path.join(MEDIA_ROOT, PHOTOGAL_THUMBS_DIR)

# Create your models here.
class Setting(models.Model):
    name = models.CharField(max_length=16, null=False, blank=False)
    value = models.CharField(max_length=256, null=False, blank=True)
    description = models.CharField(max_length=256, null=False, blank=True)

    def __str__(self):
        return self.name

class PhotoAlbums(models.Model):
    #default=Setting.objects.get(name='base_path').value
    title = models.CharField(max_length=64, null=False, blank=False)
    base_path = models.CharField(max_length=256, default=Setting.objects.get(name='base_path').value)
    tag = models.CharField(max_length=16, null=False, blank=False, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Photo Albums'
        ordering = ['title']

class PhotoCats(models.Model):
    parent = models.ForeignKey('self', null=True)
    name   = models.CharField(max_length=64, null=False, blank=False)
    path   = models.CharField(max_length=256,null=False, blank=True)
    type   = models.IntegerField(null=False, blank=False, default=0)
    album = models.ForeignKey('PhotoAlbums', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Photo Catalogs'
        ordering = ['name']

class PhotoImages(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    path = models.CharField(max_length=256, null=False, blank=False)
    filename = models.CharField(max_length=256, null=False, blank=False)
    image_date = models.DateField()
    album = models.ForeignKey('PhotoAlbums')
    cat = models.ForeignKey(PhotoCats, null=True)
    errorflag = models.IntegerField(default=0)
    rotateinfo = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Photo Images'
        ordering = ['album', 'path', 'title']

def addcat(album, rel_path):
    try:
        cat=PhotoCats.objects.get(album=album, path=rel_path)
    except PhotoCats.DoesNotExist:
        if rel_path=='':
            return None
        (head,tail)=os.path.split(rel_path)
        parent=addcat(album,head)
        cat=PhotoCats.objects.create(parent=parent,name=tail,path=rel_path, album=album)
    return cat

def addthumb(s,s_ins=PHOTOGAL_THUMB_STR):
    """Измееняет строку, содержащую имя файла изображения, вставляя '.thumb'
    перед расширением имени файлаб а расширение меняет на '.jpg'
    """
    parts= s.split(".")
    parts.insert(-1,s_ins)
    parts[-1] = 'jpg'
    return ".".join(parts)

def addimage(title,filename,path,album):
    errorflag=0
    try:
        img=PhotoImages.objects.get(album=album, path=path, filename=filename)
    except PhotoImages.DoesNotExist:
        cat=addcat(album, path)
        img=PhotoImages.objects.create(title=title, filename=filename, path=path, album=album, cat=cat, image_date=timezone.now())

    miniatures_path=os.path.join(PHOTOGAL_THUMBS_ROOT, album.tag, path)
    if not os.path.exists(miniatures_path):
        os.makedirs(miniatures_path)
    thumb_path=os.path.join(miniatures_path, addthumb(filename,PHOTOGAL_THUMB_STR))
    prev_path=os.path.join(miniatures_path, addthumb(filename,PHOTOGAL_PREV_STR))
    if not os.path.exists(thumb_path):
        full_path=os.path.join(album.base_path, path, filename)
        photo=Image.open(full_path)

        # Получаем информацию об ориентации фотографии из Exif
        exif_orientation = 0
        try:
            exif = photo._getexif()
        except:
            exif = None
            errorflag=1

        if exif != None:
            for tag, value in exif.items():
                decoded = TAGS.get(tag, tag)
                if isinstance(decoded,str):
                    if decoded.lower() == 'orientation':
                            exif_orientation = value
                            break

        # Поворачиваем фото на основании информации об ориентации
        try:
            if exif_orientation == 3: photo=photo.rotate(180)
            if exif_orientation == 6: photo=photo.rotate(270)
            if exif_orientation == 8: photo=photo.rotate(90)
        except:
            errorflag=2

        thumb=photo
        prev=photo

        # При необходимости сначала обрезаем миниатюру до квадрата
        if PHOTOGAL_THUMBS_SQUARE:
            width, height = thumb.size
            if width > height:
                delta = width - height
                left = int(delta/2)
                upper = 0
                right = height + left
                lower = height
            else:
                delta = height - width
                left = 0
                upper = int(delta/2)
                right = width
                lower = width + upper
            thumb = thumb.crop((left, upper, right, lower))

        # Создаем миниатюру и preview
        try:
            thumb.thumbnail((PHOTOGAL_THUMBS_SIZE, PHOTOGAL_THUMBS_SIZE), Image.ANTIALIAS)
            prev.thumbnail((PHOTOGAL_PREVIEW_SIZE, PHOTOGAL_PREVIEW_SIZE), Image.ANTIALIAS)
        except:
            errorflag=3


        try:
            thumb.save(thumb_path,'JPEG')
            prev.save(prev_path,'JPEG')
        except:
            errorflag=4

        img.rotateinfo=exif_orientation
        img.errorflag=errorflag
        img.save()

    return img
