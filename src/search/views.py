from django.shortcuts import render
from django.views.generic import ListView

from products.models import Product

# Create your views here.

class SearchProductView(ListView):
    template_name = "products/list.html"
    
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()