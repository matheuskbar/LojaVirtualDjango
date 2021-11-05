from django.db import models
from model_utils.models import TimeStampedModel
from localflavor.br.models import BRCPFField, BRStateField, BRPostalCodeField


class Order(TimeStampedModel):
    cpf = BRCPFField('CPF')
    name = models.CharField('Nome Completo', max_length=150)
    email = models.EmailField('E-mail', max_length=150)
    postal_code = BRPostalCodeField('CEP')
    address = models.CharField('Endereço', max_length=150)
    number = models.CharField('Número', max_length=10)
    complement = models.CharField('Complemento', max_length=150)
    district = models.CharField('Bairro', max_length=100)
    city = models.CharField('Cidade', max_length=100)
    state = BRStateField('Estado')
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'Pedido {self.id}'
