from django.db import models
from django.utils import timezone

class Cake(models.Model):
    vendor = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to = "media/")

    def __str__(self):
        return self.title     