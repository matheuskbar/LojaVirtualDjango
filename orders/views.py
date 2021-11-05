from django.shortcuts import render
from django.views.generic import CreateView

from cart.cart import Cart
from orders.forms import OrderCreateForm
from orders.models import Order, Item


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderCreateForm

    def form_valid(self, form):
        cart = Cart(self.request)
        if cart:
            order = form.save()
            # Item.objects.create(
            #     order=order,
            #     product=



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context
