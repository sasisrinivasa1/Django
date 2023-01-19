from django.db import models

class RestHotel(models.Model):
    # def __init__(self, name, desc, image):
    #     self.name = name
    #     self.desc = desc
    #     self.image = image
    # def cost(self, price):
    #     self.price = int(price)
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics',null=True)