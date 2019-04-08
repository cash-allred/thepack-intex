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
def process_request(request, cart:cmod.Sale):
    saleItems = cart.items.filter(status='A')
    print('>>>>>>>>HELLO>>>>>')


    context = {
        'cart':cart,
        'saleItems': saleItems,
    }

    return request.dmp.render('receipt.html', context)

def remove(self, product:cmod.Product):
    print('made it')
    pass

