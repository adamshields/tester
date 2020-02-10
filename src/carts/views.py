from django.shortcuts import render

def cart_home(request):
    # print(request.session) # session object is on the request object by default
    # print(dir(request.session)) # This allows me to inspect the different methods available on request.session
    # request.session.set_expiry(300) # Sets the expiration in seconds of session # 300 seconds == 5 minutes then expire this session
    # key = request.session.session_key # shows Session Key
    # print(key) # shows key only when logged in when not logged in it shows None as session Key
    # request.session['first_name'] = 'Justin'# used in example
    request.session['cart_id'] = 12 # Session Setter
    request.session['user'] = request.user.username # you can use it like this though this shows username for the session # but the object request.user OBJECT itself you can't do
    return render(request, "carts/home.html")