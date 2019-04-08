from django.db import models
from django.conf import settings
from django.utils import timezone
from decimal import Decimal
import stripe
from datetime import datetime

TAX_RATE = Decimal("0.05")

class Sale(models.Model):
    user = models.ForeignKey("account.User", on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    purchased = models.DateTimeField(null=True, default=None)
    subtotal = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
    tax = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
    total = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
    charge_id = models.TextField(null=True, default=None)   # successful charge id from stripe

    def recalculate(self):
        '''Recalculates the subtotal, tax, and total fields. Does not save the object.'''
        rTotal=0
        rTax=0
        rSubTotal=0
        items = SaleItem.objects.filter(sale=self, status='A')

        for i in items:
            st = i.price * i.quantity
            rSubTotal += st

        rTax = rSubTotal * TAX_RATE
        rTotal = rSubTotal + rTax
        self.tax = rTax
        self.total = rTotal
        self.subtotal = rSubTotal

    def finalize(self, stripeToken):        
        '''Finalizes the sale'''
        Items = SaleItem.objects.filter(sale=self, status='A')

        if self.purchased is not None:
            raise ValueError('This sale has already been finalized')

        for item in Items:
            if item.product.quantity < item.quantity:
                raise ValueError(str(item.product.name) + ' only has ' + str(item.product.quantity) + ' available.')

        self.recalculate()
        stripe.api_key = settings.STRIPE_PRIVATE_KEY
        token = stripeToken
        charge = stripe.Charge.create(
            amount = int(round(self.total, 2) * 100),
            currency='usd',
            description='Example charge',
            source=token,
        )

        self.purchased = datetime.utcnow()
        self.charge_id = charge['id'] 

        for item in Items:
            item.product.quantity = item.product.quantity - item.quantity
            item.product.save()

        self.save()


class SaleItem(models.Model):
    STATUS_CHOICES = [
        ( 'A', 'Active' ),
        ( 'D', 'Deleted' ),
    ]
    status = models.CharField(max_length=1, default=STATUS_CHOICES[0][0], choices=STATUS_CHOICES)
    sale = models.ForeignKey("Sale", on_delete=models.PROTECT, related_name="items")
    product = models.ForeignKey("Product", on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
    class Meta:
        ordering = [ 'product__name' ]


class Category(models.Model):
    last_modified = models.DateTimeField(auto_now=True)
    name = models.TextField()

class Product(models.Model):
    STATUS_CHOICES = (
        ('A','Active'),
        ('I', 'Inactive'),
    )
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.TextField(db_index=True, choices=STATUS_CHOICES, default='A')
    name = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField(default=0)
    reorder_trigger = models.IntegerField(default=0)
    reorder_quantity = models.IntegerField(default=0)


    def image_url(self):
        return self.image_urls()[0]
    
    def image_urls(self):
        prodimgs = ProductImage.objects.filter(product=self)
        urls = []
        for pi in prodimgs:
            urls.append(pi.image_url())
        if len(prodimgs) == 0:
            urls.append(settings.STATIC_URL + 'catalog/media/products/image_unavailable.gif')
        return urls

class ProductImage(models.Model):
    last_modified = models.DateTimeField(auto_now=True)
    filename = models.TextField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')

    def image_url(self):
        return settings.STATIC_URL + "catalog/media/products/" + self.filename

