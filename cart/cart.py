

class Cart:
    def __init__(self, request):
        if request.session.get('cart') in None:
            request.session['cart'] = {}

        self.cart = request.session['cart']
        self.session = request.session

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
                self.cart[product_id]['total_price'] = str(product.price * quantity)
            else:
                self.cart[product_id]['quantity'] += 1

        self.save()

    def save(self):
        self.session.modified = True
