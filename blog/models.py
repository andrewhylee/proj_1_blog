from django.db import models
from django.utils import timezone

#class Post(models.Models):
 #   title = Models.CharField(max_length=100)
# Create your models here.

class News(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.CharField(max_length = 100)
    date = models.DateField()

