from django.db import models

# Create your models here.
class Category(models.Model):  #in admin panel,automatically adds 's' to the model name 'categorys' which is wrong so can be fixed by class Meta
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True) #optional field. i.e blank is true
    cat_image = models.ImageField(upload_to='photos/categories', blank=True) #optional field. i.e blank is true

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def _str_(self):
        return self.category_name
