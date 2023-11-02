from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(unique=True)
    product_description = models.TextField(max_length=300,blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='Images/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='product')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_name}"
    
    def get_url(self):
        return reverse("product_details",args=[self.category.slug,self.slug])
    

# class Color(models.Model):
#     color = models.CharField(max_length=100)

# class Size(models.Model):
#     size = models.CharField(max_length=50)    



class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager,self).filter(variation_cat='color',is_active=True)
    def sizes(self):
        return super(VariationManager,self).filter(variation_cat='size',is_active=True)



variation_cat_choices = (
    ('color','color'),
    ('size','size')
)
class Variation(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    variation_cat = models.CharField(max_length=50,choices=variation_cat_choices)
    variation_value = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True) 
    created_date = models.DateTimeField(auto_now_add=True)
    objects = VariationManager()

    def __str__(self):
         return self.variation_value






