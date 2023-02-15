from django.db import models

# Create your models here.
class Employee(models.Model): #inherited the class(subclass-Employee) from superclass models.Model, each model is a table
    eno=models.IntegerField() #whole number using integerfield
    ename=models.CharField(max_length=30) #name using charfield with maxlength
    esal=models.FloatField()    #float numbers using FloatField
    eaddr=models.CharField(max_length=30)
#these are the instance variables of the employee class,model class has the behavior,
# what type of data ,whatever the column you give ,need to specifypython

    #django responsible for converting the fields into columns and converting model into DB Table,which is in the format of myapp_Employee is the table with extra field called id
    # model class is accomidation of columns and table
    #we need to convert this class into table for that we need sql code

#to see the created app table ,need to register this subclass into admin..py

# models.py
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='items/')

    def __str__(self):
        return self.name









