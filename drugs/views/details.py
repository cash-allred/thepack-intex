from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
from django.db.models import Avg
import math
from django.core.exceptions import ValidationError
from django import forms
from django.shortcuts import render, HttpResponseRedirect
import requests

ITEMS_PER_PAGE = 8

@view_function
def process_request(request, did):
    # drug = hmod.Drug.objects.get(id=did)
    doctors = hmod.Prescription.objects.filter(drugName_id=did)
    doctors = doctors.order_by('-quantity')
    
   

    url = "https://ussouthcentral.services.azureml.net/workspaces/e1fc1ce7a0a943dd84acf96dedd87e36/services/6c3f820a2e5144c78b6e7751773a4a8c/execute"

    querystring = {"api-version":"2.0","details":"true"}

    payload = "{\r\n  \"Inputs\": {\r\n    \"input1\": {\r\n      \"ColumnNames\": [\r\n        \"DrugName\"\r\n      ],\r\n      \"Values\": [\r\n        [\r\n          \"" + drug.drugName + "\"\r\n        ]\r\n      ]\r\n    }\r\n  }\r\n}"
    headers = {
        'Authorization': "Bearer nuPBWH3fPo2XwXNAvv4NlUIiGfqhoeqOTC9B7bJHPnmPZnjhtneu+9BQKGngEtbsuFWzJpOjP7TOXhCo+rznaA==",
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "282df8df-bf93-45a3-a9bf-b71be9cf15f1"
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    print(response.text)
    str = response.text
    relitems = str.split('"')
    print(relitems[37], relitems[39], relitems[41], relitems[43], relitems[45])
    
    links = []
    links.append(hmod.Drug.objects.get(drugName__startswith=relitems[37]))
    links.append(hmod.Drug.objects.get(drugName__startswith=relitems[39]))
    links.append(hmod.Drug.objects.get(drugName__startswith=relitems[41]))
    links.append(hmod.Drug.objects.get(drugName__startswith=relitems[43]))
    links.append(hmod.Drug.objects.get(drugName__startswith=relitems[45]))
    context={
        'drug': drug,
        'doctors': doctors,
        'relitems': relitems,
        'links': links,
    }
    
    return request.dmp.render('details.html', context)

