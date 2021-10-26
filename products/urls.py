from django.urls import path

from products.views import ProductsList, ProductDetail

app_name = 'products'

urlpatterns = [
    path('', ProductsList.as_view(), name='product-list'),
    path('<slug:slug>/', ProductDetail.as_view(), name='product-detail'),
]
