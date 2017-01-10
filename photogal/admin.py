from django.contrib import admin
from photogal.models import Setting, PhotoAlbums, PhotoImages, PhotoCats, UserProfile

# Register your models here.

class UserProfile_admin(admin.ModelAdmin):
    list_display = ('uid', 'instagram_user', 'instagram_pass')
    
class Setting_admin(admin.ModelAdmin):
    list_display = ('name', 'value', 'description')

class PhotoAlbumsAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'base_path')

class PhotoImagesAdmin(admin.ModelAdmin):
    list_display = ('album', 'title', 'path', 'filename', 'cat')
    exclude = ('image_date',)

class PhotoCatsAdmin(admin.ModelAdmin):
    list_display = ('album', 'name', 'path', 'parent')

admin.site.register(UserProfile, UserProfile_admin)
admin.site.register(Setting, Setting_admin)
admin.site.register(PhotoAlbums, PhotoAlbumsAdmin)
admin.site.register(PhotoImages, PhotoImagesAdmin)
admin.site.register(PhotoCats, PhotoCatsAdmin)