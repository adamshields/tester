from django.shortcuts import render

def cart_home(request):
    print(request.session) # session object is on the request object by default
    print(dir(request.session)) # This allows me to inspect the different methods available on request.session
    return render(request, "carts/home.html")