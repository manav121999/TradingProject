from django.db import models

# Create your models here.

class File(models.Model):
    file = models.FileField(upload_to='files')
    timeframe = models.PositiveIntegerField()

class Candles(models.Model):
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    date = models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)
    # date = models.DateField(auto_now=False, auto_now_add=False)