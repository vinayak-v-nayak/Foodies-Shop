from django.db import models

# Create your models here.

class Foodiee(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    

    updated = models.DateTimeField(auto_now=True) #updates the field value everytime instance is saved
    created = models.DateTimeField(auto_now_add=True) # sets the value whrn the instance is created.
