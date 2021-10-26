from autoslug import AutoSlugField
from django.db import models
from model_utils.models import TimeStampedModel
from stdimage import StdImageField


class Product(TimeStampedModel):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(unique=True, populate_from='name', always_update=False)
    image = StdImageField(upload_to='products/', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
