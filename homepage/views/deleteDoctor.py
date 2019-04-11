from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
from django.db.models import Avg
import math
from django.core.exceptions import ValidationError
from django import forms
from django.shortcuts import render, HttpResponseRedirect


@view_function
def process_request(request, docid):
    doctor = hmod.Doctor.objects.filter(doctorID=int(docid))
    if request.method =="POST":
        form=updateDoctor(request.POST)
        form.doctor = updateDoctor.user = request.user

        if form.is_valid():
            form.commit()
            return HttpResponseRedirect('/prescribers/')
        form = updateDoctor()
    else:
        form = updateDoctor()

    context={
        'doctor': doctor,
        'form':form,
    }
    return request.dmp.render('updateDoctor.html', context)


class deleteDoctor(forms.Form):
    
    def delete(self):
        deleteDoc = hmod.Doctor.objects.filter(doctorID=docid)
        deleteDoc.delete()


@view_function
def process_request(request):
    doctor = request.()
    print('>>>>>>>>HELLO>>>>>')
    si = cmod.SaleItem.objects.filter(sale=cart)

    context = {
        'cart':cart,
        'si': si,
    }

    return request.dmp.render('/prescribers.html', context)

def remove(self, product:cmod.Product):
    print('made it')
    pass