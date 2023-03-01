from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email', 'firstname', 'lastname', 'username', 'last_login', 'date_joined', 'is_active')
    #to set links for the fields
    list_display_links = ('email', 'first_name', 'last_name')
    # to set the fields readonly
    readonly_fields = ('last_origin', 'date_joined')
    # to show the users descending order by date
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(Account)
