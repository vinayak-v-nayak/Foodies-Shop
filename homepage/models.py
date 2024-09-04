from django.db import models

# Create your models here.

class Foodiee(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    

    updated = models.DateTimeField(auto_now=True) #updates the field value everytime instance is saved
    created = models.DateTimeField(auto_now_add=True) # sets the value when the instance is created.


class FoodImages(models.Model):

    name = models.CharField(max_length=100)
    category = models.TextField()
    cost = models.FloatField()
    images = models.ImageField(upload_to="./Food/images/")
    updated = models.DateTimeField(auto_now=True) #updates the field value everytime instance is saved
    created = models.DateTimeField(auto_now_add=True) 