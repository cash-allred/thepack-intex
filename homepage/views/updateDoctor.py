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
        form=updateDoctorForm(request.POST)
        form.doctor = updateDoctorForm.user = request.user

        if form.is_valid():
            form.commit()
            return HttpResponseRedirect('/prescribers/')
        form = updateDoctorForm()
    else:
        form = updateDoctorForm()

    context={
        'doctor': doctor,
        'form':form,
    }
    return request.dmp.render('updateDoctor.html', context)


class updateDoctorForm(forms.Form):
    FirstName = forms.CharField(widget=forms.TextInput, label='First Name', required=False)
    LastName = forms.CharField(widget=forms.TextInput, label='Last Name', required=False)
    Gender = forms.ChoiceField(choices=hmod.Doctor.STATUS_CHOICES)
    State = forms.CharField(widget=forms.TextInput, required=False)
    Credentials = forms.ChoiceField(choices=[('MD','MD'),('DO','DO'),('DMD','DMD'),('NP','NP'),('DDS','DDS'),('PA','PA'),('MED','MED'),('LPC','LPC'),('RN','RN'),('OD','OD'),('','Null')], required=False, label="Credentials")
    Specialty = forms.CharField(widget=forms.TextInput, required=False)
    OpioidPrescriber = forms.ChoiceField(choices=hmod.Doctor.OPIOID_CHOICES, label='Opioid Prescriber')
    TotalPrescriptions = forms.IntegerField(required=False)


    def clean(self):
        return self.cleaned_data

    def commit(self):
        updateDoc = hmod.Doctor.objects.filter(doctorID=0)
        updateDoc.fName = self.cleaned_data.get('FirstName')
        updateDoc.lName = self.cleaned_data.get('LastName')
        updateDoc.gender = self.cleaned_data.get('Gender')
        updateDoc.state = self.cleaned_data.get('State')
        updateDoc.credentials = self.cleaned_data.get('Credentials')
        updateDoc.opioidPrescriber = self.cleaned_data.get('OpioidPrescriber')

        updateDoc.update()

