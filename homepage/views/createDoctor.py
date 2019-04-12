from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
import math
from django.core.exceptions import ValidationError
from django import forms
from django.shortcuts import render, HttpResponseRedirect


@view_function
def process_request(request):
    doctor = hmod.Doctor
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/account/login/')
    if request.method =="POST":
        form=doctorCreateForm(request.POST)
        form.doctor = doctor
        form.user = request.user
        if not form.user.is_authenticated:
            return HttpResponseRedirect('/account/login/')
        if form.is_valid():
            form.commit()
            return HttpResponseRedirect('/')
        form = doctorCreateForm()
    
    else:
        form = doctorCreateForm()
        
    context = {
        'doctor': doctor,
        'form': form,
        jscontext('now'): datetime.now(),
    }
    return request.dmp.render('createDoctor.html', context)

class doctorCreateForm(forms.Form):
    DoctorID = forms.IntegerField(required=True, label="Doctor ID")
    FirstName = forms.CharField(widget=forms.TextInput, label='First Name', required=True)
    LastName = forms.CharField(widget=forms.TextInput, label='Last Name', required=True)
    Gender = forms.ChoiceField(choices=hmod.Doctor.STATUS_CHOICES)
    State = forms.CharField(widget=forms.TextInput, required=True)
    Credentials = forms.ChoiceField(choices=[('MD','MD'),('DO','DO'),('DMD','DMD'),('NP','NP'),('DDS','DDS'),('PA','PA'),('MED','MED'),('LPC','LPC'),('RN','RN'),('OD','OD'),('','Null')], required=True)
    Specialty = forms.CharField(widget=forms.TextInput, required=True)
    OpioidPrescriber = forms.ChoiceField(choices=hmod.Doctor.OPIOID_CHOICES, label='Opioid Prescriber')

    def clean(self):
        return self.cleaned_data

    def commit(self):
        newDoc = hmod.Doctor()
        newDoc.doctorID = self.cleaned_data.get('DoctorID')
        newDoc.fName = self.cleaned_data.get('FirstName')
        newDoc.lName = self.cleaned_data.get('LastName')
        newDoc.gender = self.cleaned_data.get('Gender')
        newDoc.state = self.cleaned_data.get('State')
        newDoc.credentials = self.cleaned_data.get('Credentials')
        newDoc.opioidPrescriber = self.cleaned_data.get('OpioidPrescriber')
        newDoc.totalPrescriptions = 0

        newDoc.save()


    