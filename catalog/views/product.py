from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod
import math
from django.core.exceptions import ValidationError
from django import forms
from django.shortcuts import render, HttpResponseRedirect

ITEMS_PER_PAGE = 8

@view_function
def process_request(request, product:cmod.Product):
    if request.method == "POST":
        #clean the form and stuff, remove the line of code below
        form=purchaseForm(request.POST)
        form.product = product
        form.user = request.user
        if not form.user.is_authenticated:
           return HttpResponseRedirect('/account/login/')
        if form.is_valid():
           form.commit()
           return HttpResponseRedirect('/catalog/cart/')

    else:
        form = purchaseForm()

    images = product.image_urls()
    context = {
        'images': images,
        'product': product,
        'form': form,
    }
    return request.dmp.render('product.html', context)

@view_function
def tile(request, product:cmod.Product):
    # just a snippet comes back
    # don't need this part any more: product = pmod.Product.object.get(id=6)
    context = {
        'product': product,
    }
    return request.dmp.render('product.tile.html', context)

class purchaseForm(forms.Form):
    quantity = forms.ChoiceField(choices=[(x, x) for x in range(1, 10)])

    def clean(self):
        if int(self.cleaned_data.get('quantity')) < self.product.quantity:
            raise ValueError(str('Only ' + str(self.quantity) + ' available.'))

        else:
            return self.cleaned_data

    def commit(self):
        cart = self.user.get_shopping_cart()
        sitems = cart.items.filter(product=self.product).first()
        if sitems is None:
            sitems = cmod.SaleItem()
            sitems.sale = cart
            sitems.product = self.product
            sitems.quantity = self.cleaned_data.get('quantity')
            sitems.price = self.product.price
            sitems.save()
        else:
            sitems.quantity += int(self.cleaned_data.get('quantity'))
            if sitems.quantity >= self.product.quantity:
                raise ValidationError('We do not have that many in stock')
            else:
                sitems.save()
        cart.recalculate()
        cart.save()