from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from cart.forms.cart_add_form import CartAddProductForm
from products.models import Product, Category


class ProductDetail(DetailView):
    queryset = Product.available.all()
    extra_context = {'form': CartAddProductForm()}


class ProductsList(ListView):
    category = None
    paginate_by = 9

    def get_queryset(self):
        queryset = Product.available.all()
        category_slug = self.kwargs.get('slug')

        if category_slug:
            self.category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=self.category)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        context["categories"] = Category.objects.all()
        return context
