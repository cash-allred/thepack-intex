from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
import math
from django.core.exceptions import ValidationError
from django import forms
from django.shortcuts import render, HttpResponseRedirect

#CREATE
#READ: reading and searching capability is taken care of with the @view_function process request
#UPDATE
#DELETE


#figure out create function!
@view_function
def process_request(request):
    prescription = hmod.Prescription
    if request.method =="POST":
        form=prescriptionCreateForm(request.POST)
        form.prescription = prescription
        form.user = request.user
        #if not form.user.is_authenticated:
            #return HttpResponseRedirect('/account/login/')
        if form.is_valid():
            form.commit()
            return HttpResponseRedirect('/')
        form = prescriptionCreateForm()
    
    else:
        form = prescriptionCreateForm()
        
    context = {
        'prescription': prescription,
        'form': form,
        jscontext('now'): datetime.now(),
    }
    return request.dmp.render('prescription.html', context)

class prescriptionCreateForm(forms.Form):
    doctorID = forms.IntegerField(label='Doctor ID', required=True)
    drugName = forms.CharField(widget=forms.TextInput, label='Drug Name', required=True)
    quantity = forms.IntegerField(label='Quantity', required=True)
    def clean(self):
        return self.cleaned_data

    def commit(self):
        newPrescription = hmod.Prescription()
        newPrescription.doctorID = self.cleaned_data('doctorID')
        newPrescription.drugName = self.cleaned_data('drugName')
        newPrescription.quantity = self.cleaned_data('quantity')

        newPrescription.save()




