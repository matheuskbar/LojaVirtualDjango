from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from products.models import Product, Category


class ProductDetail(DetailView):

    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductsList(ListView):

    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context
