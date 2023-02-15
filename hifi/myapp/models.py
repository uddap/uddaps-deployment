from django.db import models

# Create your models here.
class Employee(models.Model): #inherited the class(subclass-Employee) from superclass models.Model, each model is a table
    eno=models.IntegerField() #whole number using integerfield
    ename=models.CharField(max_length=30) #name using charfield with maxlength
    esal=models.FloatField()    #float numbers using FloatField
    eaddr=models.CharField(max_length=30)
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='items/')

    def __str__(self):
        return self.name

