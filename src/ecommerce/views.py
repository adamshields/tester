from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm

def home_page(request):
    context = {
        "title": "Home Page",
        "content": "Welcome to the Home Page",
    }
    return render(requests, "home_page.html", context)

def about_page(request):
    context = {
        "title": "About Us",
        "content": "Welcome to the About Page",
    }
    return render(requests, "home_page.html", context)

def login_page(request):
    return render(request, "auth/login.html", {})

def register_page(request):
    return render(request, "auth/register.html", {})



def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact",
        "content": "Welcome to the Contact Page",
        "form": contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     # print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "contact/view.html", context)

# def home_page(requests):
#     return render(requests, "home_page.html")