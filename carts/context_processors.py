from .models import CartItem,Cart
from .views import _cart_id


def counter(request):
    count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all()
            cart_items = cart_items.filter(cart=cart)
            for cart_item in cart_items:
                count += cart_item.quantity
        except:
            count = 0


        return {"count":count}
