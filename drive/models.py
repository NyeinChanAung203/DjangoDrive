from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Folder(models.Model):
    foldername = models.CharField(max_length=50)
    description = models.CharField(max_length=200,blank=True,null=True)
    folderuser = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.foldername)


class File(models.Model):
    filename = models.CharField(max_length=100)
    file = models.FileField(upload_to='Files')
    folder = models.ForeignKey(Folder,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.filename)