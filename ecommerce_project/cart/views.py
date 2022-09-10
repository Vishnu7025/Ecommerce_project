from django.shortcuts import render,redirect,get_object_or_404
from .models import Cart,CartItem, Review
from home.models import products
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request,product_id):
    product = products.objects.get(id=product_id) #get the product
    try:
        cart  = Cart.objects.get(cart_id =_cart_id(request))#get the cart using cart_id present in the session
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save

    try:
        cart_item = CartItem.objects.get(product=product,cart=cart)
        cart_item.quantity += 1 #cart_item.quantity = cart_item.quantity + 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity= 1,
            cart = cart,
        )
        cart_item.save()
    return redirect('cart')

def remove_cart(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(products,id=product_id)
    cart_item = CartItem.objects.get(product=product,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def remove_cart_item(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(products,id=product_id)
    cart_item = CartItem.objects.get(product=product,cart=cart)
    cart_item.delete()
    return redirect('cart')


def cart(request, total=0,quantity=0,cart_items=None,tax=0,grand_total=0):
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
    
    context = {
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'tax':tax,
        'grand_total':grand_total,
    }
    
    return render(request,'cart.html',context)


def order(request):

    return render(request,'placeorder.html')

def Review_rate(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        product = products.objects.get(id=prod_id)
        comment = request.GET.get('comment')
        rate = request.GET.get('rate')
        user = request.user 
        Review(user=user,product= product,comment=comment,rate=rate).save()
        return redirect('/')


