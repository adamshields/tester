from django.shortcuts import render

def cart_home(request):
    cart_id = request.session.get("cart_id", None) # this says get the current cart id or none
    if cart_id is None and isinstance(cart_id, int): # isinstance allows us to compare with python, so you want to make sure the object is type of that class
        print('Create New Cart')
        request.session['cart_id'] = 12 # This is where we actually set it 
    else:
        print('Cart ID Exists')
    return render(request, "carts/home.html")