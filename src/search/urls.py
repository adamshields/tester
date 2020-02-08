from django.urls import path, re_path

from products.views import (
    ProductListView,
    )

app_name="search"


urlpatterns = [
    path('', ProductListView.as_view(), name='list'),

]
