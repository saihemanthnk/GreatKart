from django.shortcuts import render,redirect,get_object_or_404
from store.models import Product
from .models import Cart,CartItem
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Variation

# Create your views here.



def cart(request):
    total = 0
    quantity = 0
    cart_items = None
    grand_total = 0 
    tax = 0

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request)) 
        cart_items = CartItem.objects.filter(cart=cart,is_active=True)
        for cart_item in cart_items:
            total += cart_item.product.price * cart_item.quantity
            quantity += cart_item.quantity



        tax = (5 * total)/100
        grand_total = total + tax 
    except ObjectDoesNotExist:
        pass

    context = {
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'grand_total':grand_total,
        'tax':tax
    }



  

    return render(request,'store/cart.html',context)


def _cart_id(request):
    cart_id = request.session.session_key
    if not cart_id:
        cart_id = request.session.create()
    return cart_id


def add_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    product_variation_list = []
    
    if request.method == 'POST':
         for item in request.POST:
             key = item 
             value = request.POST[key]

        
           
            
             try:
                  variation = Variation.objects.get(variation_cat__iexact=key,variation_value__iexact=value,product=product)
                  product_variation_list.append(variation) 
                
             except:
                 pass
                
    # return HttpResponse(product_variation_list)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()

    is_cart_item = CartItem.objects.filter(product=product,cart=cart).exists()
    if is_cart_item:

        cart_items = CartItem.objects.filter(cart=cart,product=product)
        existing_cart_items_list = [] # data-base
        id = []

        for item in cart_items:
            existing_cart_items=item.variations.all()
            existing_cart_items_list.append(list(existing_cart_items))
            id.append(item.id)




        if product_variation_list in existing_cart_items_list:
            # increase quantity 
            index = existing_cart_items_list.index(product_variation_list)
            id1 = id[index]
            item = CartItem.objects.get(product=product,id=id1)
            item.quantity +=1 
            item.save()
        else:
            item = CartItem.objects.create(product=product,quantity=1,cart=cart)
            
            if len(product_variation_list)>0:
                    item.variations.clear()
                    for i in product_variation_list:
                        item.variations.add(i)
        
            item.save()

    else:
        item = CartItem.objects.create(cart=cart,product=product,quantity=1)

        if len(product_variation_list)>0:
            item.variations.clear()
            for i in product_variation_list:
                item.variations.add(i)

        item.save()

        
    return redirect("cart")


def remove_cart_item(request,product_id,id2):
    product = Product.objects.get(id=product_id)
    cart = get_object_or_404(Cart,cart_id = _cart_id(request))
    cart_item = CartItem.objects.get(product=product,cart=cart,id=id2)
    cart_item.delete()
    
    return redirect("cart")
    



def remove_cart(request,product_id,id2):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_item = CartItem.objects.get(cart=cart,product=product,id=id2)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
       
    return redirect("cart")




