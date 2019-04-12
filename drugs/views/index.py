from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
from django.core.exceptions import ValidationError
from django import forms
from django.shortcuts import render, HttpResponseRedirect

@view_function
def process_request(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/account/login/')

    #this is where I search
    if request.method == "POST":
    #clean the form and stuff, remove the line of code below
        form=drugSearchForm(request.POST)
        if form.is_valid():
            drugs = hmod.Drug.objects.filter(drugName__contains=form.cleaned_data['drugName'])
            drugs = drugs.filter(isOpioid__contains=form.cleaned_data['isOpioid'])
    
    else:
        drugs = '' #hmod.Drug.objects.all()

    form = drugSearchForm()
    context={
        'drugs': drugs,
        'form': form,
    }
    return request.dmp.render('index.html', context)

class drugSearchForm(forms.Form):
    drugName = forms.CharField(widget=forms.TextInput, label='Drug Name', required=False)
    isOpioid = forms.ChoiceField(choices=[('1','Yes'),('0','No'),('','Null')], label ='Is an Opioid', required=False)
    
    def clean(self):
        return self.cleaned_data