from.models import Cart,CartItem, Review
from .  views import _cart_id
from django.core.exceptions import ObjectDoesNotExist

def counter(request):
    cart_count =0
    if 'admin' in request.path:
        return{}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            cart_items= CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except Cart.DoesNotExist:
            cart_count=0
    return dict(cart_count=cart_count)


def order(request ,total=0,quantity=0,cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items=CartItem.objects.filter(cart=cart,is_active=True)
        for cart_item in cart_items:
           total += (cart_item.product.price * cart_item.quantity)
           quantity += cart_item.quantity
        tax =(2 * total)/100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass# just ignore
        grand_total=0
 
    return dict(grand_total=grand_total)

def review(request):
    review=Review.objects.filter()
    return dict(review=review)