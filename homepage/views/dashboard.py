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
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/account/login/')
    if request.user.user_type == 1:
        return HttpResponseRedirect('/account/denied/')
    context = {
        jscontext('now'): datetime.now(),
    }
    return request.dmp.render('dashboard.html', context)