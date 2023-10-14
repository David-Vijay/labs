from django.db import models
import datetime, os
# Create your models here.
class addImg(models.Model):
    photo=models.ImageField(upload_to='images')
    name=models.CharField(max_length=20)
    points=models.IntegerField()
    def __str__(self):
        return self.name