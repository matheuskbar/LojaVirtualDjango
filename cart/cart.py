import copy
from decimal import Decimal

from products.models import Product


class Cart:
    def __init__(self, request):
        if request.session.get('cart') is None:
            request.session['cart'] = {}

        self.cart = request.session['cart']
        self.session = request.session

    def __iter__(self):
        cart = copy.deepcopy(self.cart)

        products = Product.objects.filter(id__in=cart)
        for product in products:
            cart[str(product.id)]["product"] = product

        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["quantity"] * item["price"]
            # item["update_quantity_form"] = CartAddProductForm(
            #     initial={"quantity": item["quantity"], "override": True}
            # )

            yield item

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price),
                'total_price': str(product.price),
            }
            if override_quantity:
                self.cart[product_id]['quantity'] = quantity
            else:
                self.cart[product_id]['quantity'] += quantity

            self.cart[product_id]['total_price'] = str(product.price * quantity)

        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session.modified = True
