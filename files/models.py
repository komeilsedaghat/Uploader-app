from django.db import models
from account.models import User
# Create your models here.

class FileModel(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    file = models.FileField()

    def __str__(self):
        return f"{self.user} - {self.text}"