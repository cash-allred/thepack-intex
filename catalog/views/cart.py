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
def process_request(request):
    cart = request.user.get_shopping_cart()
    print('>>>>>>>>HELLO>>>>>')
    si = cmod.SaleItem.objects.filter(sale=cart)

    context = {
        'cart':cart,
        'si': si,
    }

    return request.dmp.render('cart.html', context)

def remove(self, product:cmod.Product):
    print('made it')
    pass

