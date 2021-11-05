from django import forms

from orders.models import Order


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [
            'cpf',
            'name',
            'email',
            'postal_code',
            'address',
            'number',
            'complement',
            'district',
            'city',
            'state',
        ]
