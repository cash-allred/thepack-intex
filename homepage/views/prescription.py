from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
import math
from django.core.exceptions import ValidationError
from django import forms
from django.shortcuts import render, HttpResponseRedirect

#CREATE:
#READ: reading and searching capability is taken care of with the @view_function process request
#UPDATE
#DELETE


#figure out create function!
@view_function
def process_request(request, docid):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/account/login/')
        
    prescription = hmod.Prescription
    drug = hmod.Drug.objects.all()
    doctor = hmod
    if request.method =="POST":
        form=prescriptionCreateForm(request.POST)
        form.prescription = prescription
        form.user = request.user
        #if not form.user.is_authenticated:
            #return HttpResponseRedirect('/account/login/')
        if form.is_valid():
            form.commit(docid)
            return HttpResponseRedirect('/')
        form = prescriptionCreateForm()
    
    else:
        form = prescriptionCreateForm()
        
    context = {
        'prescription': prescription,
        'form': form,
        'drug': drug,
        jscontext('now'): datetime.now(),
    }
    return request.dmp.render('prescription.html', context)

class prescriptionCreateForm(forms.Form):
    drug = hmod.Drug.objects.all()

    # DRUG_CHOICES = {
    #     for d in drug:
    #         print (d.drugName.ID, d.drugName)
    #         pass    
    # }
    drugName = forms.CharField(widget=forms.TextInput, label='Drug Name', required=True)
    quantity = forms.IntegerField(label='Quantity', required=True)
    
    def clean(self):
        return self.cleaned_data

    def commit(self, docid):
        #create new prescription
        newPrescription = hmod.Prescription()
        newPrescription.doctorID = docid
        newPrescription.drugName.id = self.cleaned_data('drugName')
        newPrescription.quantity = self.cleaned_data('quantity')

        newPrescription.save()
        
        #update prescription total for doctor
        updatedDocPrescriptions = hmod.Doctor.objects.get(doctorID=docID)

        updatedDocPrescriptions.totalPrescriptions += self.cleaned_data('quantity')
        updatedDocPrescriptions.save()



