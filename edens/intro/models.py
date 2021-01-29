from django.db import models

# Create your models here.
class newArrivals(models.Model):
    title = models.CharField(max_length=250)
    discription = models.CharField(max_length=250)
    price = models.FloatField()
    img_url = models.CharField(max_length=3000)

class offers(models.Model):
    title = models.CharField(max_length=240)
    img_url = models.CharField(max_length= 3000)
    price = models.FloatField()