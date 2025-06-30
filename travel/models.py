from django.db import models

# Create your models here.
class Destination(models.Model):
    name=models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics')
    desc=models.TextField()

class ThingToDo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    img = models.ImageField(upload_to='things_to_do')
