from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
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
            for item in cart:
                Item.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                    price=item['price']
                )
            return render(self.request, 'orders/order_create.html', {'order': order})
        return HttpResponseRedirect(reverse('products:list'))


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context
