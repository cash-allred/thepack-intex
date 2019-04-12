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
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/account/login/')

    if not request.user.user_type == 1:
        return HttpResponseRedirect('/account/denied/')
        
    doctor = hmod.Doctor.objects.get(doctorID=docid)
    initial = {
        'doctorID':doctor.doctorID,
        'FirstName': doctor.fName,
        'LastName': doctor.lName,
        'Gender': doctor.gender,
        'State': doctor.state,
        'Credentials': doctor.credentials,
        'OpioidPrescriber': doctor.opioidPrescriber,
        'TotalPrescriptions': doctor.totalPrescriptions,
    }
    if request.method =="POST":
        form=updateDoctor(request.POST)
        form.doctor = updateDoctor.user = request.user

        if form.is_valid():
            form.commit(docid)
            return HttpResponseRedirect('/prescribers/')
        form = updateDoctor()
    else:
        form = updateDoctor()

    context={
        'doctor': doctor,
        'form': form,
    }
    return request.dmp.render('updateDoctor.html', context)

class updateDoctor(forms.Form):
    FirstName = forms.CharField(widget=forms.TextInput, label='First Name', required=False)
    LastName = forms.CharField(widget=forms.TextInput, label='Last Name', required=False)
    Gender = forms.ChoiceField(choices=hmod.Doctor.STATUS_CHOICES)
    State = forms.CharField(widget=forms.TextInput, required=False)
    Credentials = forms.ChoiceField(choices=[('MD','MD'),('DO','DO'),('DMD','DMD'),('NP','NP'),('DDS','DDS'),('PA','PA'),('MED','MED'),('LPC','LPC'),('RN','RN'),('OD','OD'),('','Null')], required=False, label="Credentials")
    Specialty = forms.CharField(widget=forms.TextInput, required=False)
    OpioidPrescriber = forms.ChoiceField(choices=hmod.Doctor.OPIOID_CHOICES, label='Opioid Prescriber')
    TotalPrescriptions = forms.IntegerField(required=False, label = "Total Prescriptions")


    def clean(self):
        return self.cleaned_data

#still doesn't actually update
    def commit(self, docid):
        doctor = hmod.Doctor.objects.get(doctorID=docid)
        if self.cleaned_data.get('FirstName') != "":
            doctor.fName = self.cleaned_data.get('FirstName')
        if self.cleaned_data.get('LastName') !="":
            doctor.lName = self.cleaned_data.get('LastName')
        if self.cleaned_data.get('Gender') !="":
            doctor.gender = self.cleaned_data.get('Gender')
        if self.cleaned_data.get('State') !="":
            doctor.state = self.cleaned_data.get('State')
        if self.cleaned_data.get('Credentials') !="":
            doctor.credentials = self.cleaned_data.get('Credentials')
        if self.cleaned_data.get('OpioidPrescriber') !="":
            doctor.opioidPrescriber = self.cleaned_data.get('OpioidPrescriber')
        if self.cleaned_data.get('TotalPrescriptions') !="":
            doctor.totalPrescriptions = self.cleaned_data.get('TotalPrescriptions')
       
        doctor.save()


