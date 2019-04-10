from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
from django.db.models import Avg
import math
from django.core.exceptions import ValidationError
from django import forms
from django.shortcuts import render, HttpResponseRedirect

ITEMS_PER_PAGE = 8

@view_function
def process_request(request, did):
    drug = hmod.Drug.objects.get(id=did)
    doctors = hmod.Prescription.objects.filter(drugName_id=did)
    doctors = doctors.order_by('-quantity')
    context={
        'drug': drug,
        'doctors': doctors,
    }
    return request.dmp.render('details.html', context)

