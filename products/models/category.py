from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(unique=True, populate_from='name', always_update=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('people-detail', kwargs={'pk': self.pk})
