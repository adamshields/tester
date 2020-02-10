from django.shortcuts import render


from .models import Cart

def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    return cart_obj

def cart_home(request):
    request.session['cart_id'] = "12"
    cart_id = request.session.get("cart_id", None) 
    if cart_id is None and isinstance(cart_id, int): 
        cart_obj = cart_create()
        request.session['cart_id'] = cart_obj.id 
        print('New Cart Created')
    else:
        print('Cart ID Exists')
        print(cart_id)
        cart_obj = Cart.objects.get(id=cart_id)
    return render(request, "carts/home.html")
