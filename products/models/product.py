from autoslug import AutoSlugField
from django.db import models
from model_utils.models import TimeStampedModel
from stdimage import StdImageField

from products.models import Category


class AvailableManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)


class Product(TimeStampedModel):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(unique=True, populate_from='name', always_update=False)
    image = StdImageField(upload_to='products/', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, blank=True, null=True)

    objects = models.Manager()
    available = AvailableManager()

    def __str__(self):
        return self.name
