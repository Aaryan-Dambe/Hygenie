from django.db import models

# Create your models here.
class profit(models.Model):
    name = models.CharField(max_length=25)
    disc = models.TextField(max_length=1000)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)




