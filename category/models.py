from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=250,blank=True)
    cat_img = models.ImageField(upload_to='Images/categories',blank=True)
    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return f"{self.category_name}"
    
    
   



