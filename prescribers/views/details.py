from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
from django.db.models import Avg
import math
from django.core.exceptions import ValidationError
from django import forms
from django.shortcuts import render, HttpResponseRedirect
import http.client
import requests



ITEMS_PER_PAGE = 8

@view_function
def process_request(request, docid):
    doctor = hmod.Doctor.objects.filter(doctorID=int(docid))
    prescriptions = hmod.Prescription.objects.filter(doctorID=int(docid))
    average = {}
    avgs1 = []
    ave = []
    str1 = str
    str2 = str
    for script in prescriptions:
        average[script.drugName]=hmod.Prescription.objects.filter(drugName=int(script.drugName_id)).aggregate(Avg('quantity'))
        avgs1.append(str1(average[script.drugName]))
    
    url = "https://ussouthcentral.services.azureml.net/workspaces/e1fc1ce7a0a943dd84acf96dedd87e36/services/d31c28dd22324b28a6fe09d906d463a7/execute"

    querystring = {"api-version":"2.0","details":"true"}

    payload = "{\r\n  \"Inputs\": {\r\n    \"input1\": {\r\n      \"ColumnNames\": [\r\n        \"PrescriberID\"\r\n      ],\r\n      \"Values\": [\r\n        [\r\n          \"" + docid + "\"\r\n        ]\r\n      ]\r\n    }\r\n  }\r\n}"
    headers = {
        'Authorization': "Bearer 2SLH+GczCmRWIPpvwwsnQ8baMSxirbr/tPd5HH0CRVadzG/cPsgkIii023BNmZaFjHWIjpDM7FryAT2f6tPQnw==",
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "b30756fd-df4f-4ec5-9529-93dfda028289"
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)


    print(response.text)
    str2 = response.text
    relusers = str2.split('"')
    print(relusers[37], relusers[39], relusers[41], relusers[43], relusers[45])
    print(avgs1)    
    


    context={
        'doctor': doctor,
        'prescriptions': prescriptions,
        'average': average,
        'relusers': relusers,
        'avgs1': avgs1,
        
    }
    return request.dmp.render('details.html', context)

