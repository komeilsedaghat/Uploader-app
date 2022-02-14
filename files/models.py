from django.db import models
from django.forms import ValidationError
from account.models import User
# Create your models here.

class FileModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.CharField(max_length=200,blank=True)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.user} - {self.text}"


class VideoModel(FileModel):
    file = models.FileField(upload_to='video/')

    class Meta:
        ordering = ['-time']

class ImageModel(FileModel):
    file = models.ImageField(upload_to = 'image/')

    class Meta:
        ordering = ['-time']

