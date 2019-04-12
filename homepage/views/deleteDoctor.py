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
        form=deleteDoctor(request.POST)
        form.delete(docid)
        form.save()
        # if form.is_valid():
        #     form.commit()
        #     return HttpResponseRedirect('/prescribers/')
        # form = deleteDoctor(docid)
    else:
        form = deleteDoctor(docid)

    context={
        'doctor': doctor,
        'form':form,
    }
    return request.dmp.render('deleteDoctor.html', context)


class deleteDoctor(forms.Form):
    def delete(self, docid):
        deleteDoc = hmod.Doctor.objects.filter(doctorID=docid)
        deleteDoc.delete()
