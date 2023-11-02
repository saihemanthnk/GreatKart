from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Product,Variation
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id 
from django.db.models import Q

from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.

def store(request,slug=None):
    products = Product.objects.all().filter(is_available=True).order_by('id')
    paginator = Paginator(products,3)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)



    pod_count = products.count()
    categories = Category.objects.all()
    if slug!=None:
       category = Category.objects.get(slug=slug)
       products_by_cat = category.product.all()
       av_products_by_cat = products_by_cat.filter(is_available=True)
       paginator = Paginator(av_products_by_cat,1)
       page = request.GET.get('page')
       paged_products = paginator.get_page(page)
       count = av_products_by_cat.count()

       return render(request,"store/store.html",{"products":paged_products,'pod_count':count,'categories':categories})
       
    
    return render(request,"store/store.html",{"products":paged_products,'pod_count':pod_count,'categories':categories})


def product_details(request,slug1,slug2):
    # category = Category.objects.get(slug=slug1)
    # products = category.product.all() jk
    # for product in products:
    #     if product.slug == slug2:
    #         data = product  // approch 1

    data = Product.objects.get(category__slug=slug1,slug=slug2)
    

    try:

        in_cart = CartItem.objects.filter(product=data,cart__cart_id=_cart_id(request)).exists()
        # in_cart = CartItem.objects.get(product__slug=slug2)

    except:
        in_cart = False


    return render(request,"store/product_detail.html",{"product":data,'in_cart':in_cart})

def search(request):
    

    if 'keyword' in request.GET:
        search_value = request.GET.get('keyword')
        
        
        products = Product.objects.filter(Q(product_name__icontains=search_value)|Q( product_description__icontains=search_value)).order_by('-created_date')
        pod_count = products.count()


    return render(request,'store/store.html',{'products':products,'pod_count':pod_count})

