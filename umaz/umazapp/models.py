from django.contrib.auth.models import User, Permission, Group
from django.db import models

# Create your models here.
# class User(AbstractUser):
#     email = models.EmailField(unique=True)

class User(models.Model):

    username = models.CharField(max_length=250, unique=True)
    email = models.EmailField(unique=True)
    password1 = models.CharField(max_length=250,unique=True)
    password2 = models.CharField(max_length=250,unique=True)
    groups = models.ManyToManyField(
        Group,
        related_name='umaz_user_set',
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='umaz_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

