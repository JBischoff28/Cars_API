from django.db import models  # This file is used tocreate models, which translate to tables in the database

# Create your models here.

class Car(models.Model): 
    make = models.CharField(max_length=255) # Each row here represents the different columns a database table
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)# ^^^^