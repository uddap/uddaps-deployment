from django.contrib import admin
from myapp.models import Employee

#Register your models here.
class EmployeeAdmin(admin.ModelAdmin): #to display some data on django admin UI
    # in browser,now write views to get data from DB and then send data to template
    list_display=['eno', 'ename', 'esal', 'eaddr']
admin.site.register(Employee)


# to Login to admin UI ,need to create super user,what info need to provide
# python3 manage.py createsuperuser
# python3 manage.py runserver
# http://127.0.0.1:8000/admin