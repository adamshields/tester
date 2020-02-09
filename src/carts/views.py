from django.shortcuts import render

def cart_home(request):
    print(request.session) # session object is on the request object by default
    return render(request, "carts/home.html")