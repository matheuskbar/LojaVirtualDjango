from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from cart.cart import Cart
from products.models import Product


def cart_detail(request):
    return render(request, 'cart/cart_detail.html')

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    cart.add(
        product=product
    )

    return redirect("cart:detail")
