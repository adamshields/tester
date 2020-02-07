
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include

# from products.views import (
#     ProductDetailSlugView, ProductDetailView, ProductFeaturedDetailView,
#     ProductFeaturedListView, ProductListView, product_detail_view,
#     product_list_view)

from .views import (about_page, contact_page, home_page, login_page,
                    register_page)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('about/', about_page),
    path('contact/', contact_page),
    path('login/', login_page),
    path('register/', register_page),
    path('products/', include('products.urls')),
    # re_path(r'^featured/$', ProductFeaturedListView.as_view()),
    # re_path(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
    # path('products/', ProductListView.as_view()),
    # path('products-fbv', product_list_view),
    # # re_path(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()), # This is the Private Key View Commented out No Longer Needed since using slugs
    # re_path(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
    # re_path(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
