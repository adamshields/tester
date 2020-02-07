from django.urls import path, re_path

from .views import (
    ProductDetailSlugView, 
    ProductListView,
    )

urlpatterns = [
    path('', ProductListView.as_view()),
    path('<slug:slug>/', ProductDetailSlugView.as_view(), name='product_detail_slug'),
]
