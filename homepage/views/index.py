from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime
from account import models as amod
from catalog import models as cmod
from django.shortcuts import render, HttpResponseRedirect

@view_function
def process_request(request):

    #used to create the users
    # u = amod.User()
    # u.username = 'SampleHealthOfficial'
    # u.first_name = 'Health'
    # u.last_name = 'Official'
    # u.email = 'HealthOfficial@test.com'
    # u.birthdate = datetime(2011, 1, 1)
    # u.set_password('asdf')
    # u.user_type = '2'
    # u.save()

    # u2 = amod.User()
    # u2.username = 'SampleDataClerk'
    # u2.first_name = 'Data'
    # u2.last_name = 'Clerk'
    # u2.email = 'DataClerk@test.com'
    # u2.birthdate = datetime(2011, 1, 1)
    # u2.set_password('asdf')
    # u2.user_type = '1'
    # u2.save()

    # u3 = amod.User()
    # u3.username = 'SampleDoctor'
    # u3.first_name = 'Dr.'
    # u3.last_name = 'Doctor'
    # u3.email = 'Doctor@test.com'
    # u3.birthdate = datetime(2011, 1, 1)
    # u3.set_password('asdf')
    # u3.user_type = '3'
    # u3.save()

    if not request.user.is_authenticated:
        return HttpResponseRedirect('/account/login/')

    context = {
        jscontext('now'): datetime.now(),
    }
    return request.dmp.render('index.html', context)

