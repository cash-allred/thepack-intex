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
def process_request(request, docid):
    doctor = hmod.Doctor.objects.filter(doctorID=int(docid))
    prescriptions = hmod.Prescription.objects.filter(doctorID=int(docid))
    average = {}
    for script in prescriptions:
        average[script.drugName]=hmod.Prescription.objects.filter(drugName=int(script.drugName_id)).aggregate(Avg('quantity'))
    
    context={
        'doctor': doctor,
        'prescriptions': prescriptions,
        'average': average,
    }
    return request.dmp.render('details.html', context)

