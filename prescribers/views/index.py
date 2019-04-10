from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
import math
from django.core.exceptions import ValidationError
from django import forms
from django.shortcuts import render, HttpResponseRedirect

ITEMS_PER_PAGE = 8

@view_function
def process_request(request):
    #this is where I figure out search
    if request.method == "POST":
    #clean the form and stuff, remove the line of code below
        form=doctorSearchForm(request.POST)
        if form.is_valid():
            doctors = hmod.Doctor.objects.filter(fName__contains=form.cleaned_data['firstName'])
            doctors = doctors.filter(lName__contains=form.cleaned_data['lastName'])
            doctors = doctors.filter(gender__contains=form.cleaned_data['gender'])
            doctors = doctors.filter(state__contains=form.cleaned_data['state'])
            doctors = doctors.filter(credentials__contains=form.cleaned_data['credentials'])
            doctors = doctors.filter(specialty__contains=form.cleaned_data['specialty'])
    else:
        doctors = hmod.Doctor.objects.all()
    #numpages = math.ceil(doctors.count()/ ITEMS_PER_PAGE)
    #doctors = doctors[(page-1) * ITEMS_PER_PAGE: page * ITEMS_PER_PAGE]
    form = doctorSearchForm() 
    context={
        'doctors': doctors,
        'form':form,
        #'page': page,
        #'numpages': numpages,
    }
    return request.dmp.render('index.html', context)

class doctorSearchForm(forms.Form):
    firstName = forms.CharField(widget=forms.TextInput, label='First Name', required=False)
    lastName = forms.CharField(widget=forms.TextInput, label='Last Name', required=False)
    gender = forms.ChoiceField(choices=[('M','Male'),('F','Female'),('','Null')], required=False)
    credentials = forms.ChoiceField(choices=[('MD','MD'),('DO','DO'),('DMD','DMD'),('NP','NP'),('DDS','DDS'),('PA','PA'),('MED','MED'),('LPC','LPC'),('RN','RN'),('OD','OD'),('','Null')], required=False)
    state = forms.CharField(widget=forms.TextInput, required=False)
    specialty = forms.CharField(widget=forms.TextInput, required=False)

    def clean(self):
        return self.cleaned_data