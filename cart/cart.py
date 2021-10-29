

class Cart:
    def __init__(self, request):
        if request.session.get['cart'] in None:
            request.session['cart'] = {}

        self.cart = request.session['cart']
        self.session = request.session

    def add(self, product, quantity=1):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 1,
                'price': str(product.price)
            }
        self.session.modified = True
