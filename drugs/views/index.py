from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
from django.core.exceptions import ValidationError
from django import forms
from django.shortcuts import render, HttpResponseRedirect

@view_function
def process_request(request):
    drugs = hmod.Drug.objects.all()

    context={
        'drugs': drugs,
    }
    return request.dmp.render('index.html', context)


