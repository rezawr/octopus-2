from django.db import models
from django.utils.translation import gettext_lazy as _

from model_utils import Choices


STATUS = Choices(
    ('pending', _('Pending')), 
    ('shipping', _('Shipping'))
)

class Product(models.Model):
    name = models.CharField(_('Product name'), max_length=100)
    price = models.FloatField(_('Product price'))


class Seller(models.Model):
    name = models.CharField(_('Seller name'), max_length=100)


class Buyer(models.Model):
    name = models.CharField(_('Buyer name'), max_length=100)


class Order(models.Model):
    buyer = models.ForeignKey(
        Buyer,
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Seller,
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(_('Quantity'))
    status = models.CharField(_('Order status'), choices=STATUS, default=STATUS.pending, max_length=10)
    shipping_code = models.CharField(_('Shipping code'), max_length=25, default=None, blank=True, null=True)
