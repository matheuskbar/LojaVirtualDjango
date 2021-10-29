from django.urls import path

from products.views import ProductsList, ProductDetail

app_name = 'products'

urlpatterns = [
    path('', ProductsList.as_view(), name='list'),
    path("category/<slug:slug>/", ProductsList.as_view(), name="list_by_category"),
    path('<slug:slug>/', ProductDetail.as_view(), name='detail'),
]
