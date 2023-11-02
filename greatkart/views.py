from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product
from category.models import Category


# def home(request):
#     return HttpResponse("Home page")


def home(request):
    products = Product.objects.all().filter(is_available=True)
   

    return render(request,"home.html",{"products":products})
