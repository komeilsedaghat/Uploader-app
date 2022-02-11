from django.db import models
from django.forms import ValidationError
from account.models import User
# Create your models here.

class FileModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.CharField(max_length=200,blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.user} - {self.text}"


class VideoModel(FileModel):
    file = models.FileField()

class ImageModel(FileModel):
    file = models.ImageField()

