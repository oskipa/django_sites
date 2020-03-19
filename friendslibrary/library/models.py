from django.db import models
# Create your models here.

class ItemType(models.Model):
    name = models.CharField(40)

class Item(models.Model):
    name = models.CharField(max=200)
    description = models.TextField()
    type = models.ForeignKey( ItemType, on_delete=models.DO_NOTHING)
    owner = models.ForeignKey( User, on_delete=models.CASCADE)
    location = models.ForeignKey( User, on_delete=models.PROTECT)

