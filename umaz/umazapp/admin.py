from django.contrib import admin
from umazapp.models import User

#Register your models here.
class UserAdmin(admin.ModelAdmin): #to display some data on django admin UI
    # in browser,now write views to get data from DB and then send data to template
    list_display=['username', 'email', 'password1', 'password2']
admin.site.register(User)


# to Login to admin UI ,need to create super user,what info need to provide
# python3 manage.py createsuperuser
# python3 manage.py runserver
# http://127.0.0.1:8000/admin