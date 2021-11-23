from django.db import models
#from django.db.models.fields import DatetimeField
#from datetime import datetime
from django.utils.timezone import now

# Create your models here.
class Gifs(models.Model):
    title = models.CharField(max_length = 50)
    url = models.URLField(max_length= 25)
    uploader_name = models.CharField(max_length=50)
    created_at = models.DateTimeField()

class Category(models.Model):
    name = models.CharField(max_length=50)
    gifs = models.ManyToManyField(Gifs, related_name='categories', blank=True)