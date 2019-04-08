from django.conf import settings
from django_mako_plus import view_function, jscontext
from account.forms import loginForm
from account import models as amod
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django import forms
from django.shortcuts import render, HttpResponseRedirect


@view_function
def process_request(request):

    # if it is a post method
    if request.method == 'POST':

        #create the form instance and populate it with the data from the form
        form = loginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            login(request, user)
            return HttpResponseRedirect('/')

        else:
            return request.dmp.render('login.html', {'form': form,})

    # if it is a get method
    else:
        form = loginForm()

    context = {
        'form':form,
    }

    return request.dmp.render('login.html', context)

    
