from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    des = models.TextField()
    def __str__(self):
        return self.name


class Name(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='img')
    des = models.TextField()

    def __str__(self):
        return self.name