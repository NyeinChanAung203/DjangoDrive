from django.contrib import admin
from .models import Folder,File
# Register your models here.

class AdminFolder(admin.ModelAdmin):
    list_display = ('foldername','folderuser')

class AdminFile(admin.ModelAdmin):
    list_display = ('filename','file')

admin.site.register(Folder,AdminFolder)
admin.site.register(File,AdminFile)