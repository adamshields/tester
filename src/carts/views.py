from django.shortcuts import render


from .models import Cart


def cart_home(request):
    cart_id = request.session.get("cart_id", None) # this says get the current cart id or none
    if cart_id is None: # and isinstance(cart_id, int): # isinstance allows us to compare with python, so you want to make sure the object is type of that class
        # print('Create New Cart')
        cart_obj = Cart.objects.create(user=None)
        request.session['cart_id'] = cart_obj.id # set cart_obj.id to session
        print(cart_obj.id) # shows actualdynamic cart id for session
    else:
        print('Cart ID Exists')
        print(cart_id)
        cart_obj = Cart.objects.get(id=cart_id)
    return render(request, "carts/home.html")