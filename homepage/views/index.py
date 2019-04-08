from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime
from account import models as amod
from catalog import models as cmod

@view_function
def process_request(request):

    #used to create the users
    #for (i) in range(10):
       #u = amod.User()
       #u.username = f'user{i}'
       #u.first_name = 'first' + str(i)
       #u.last_name = 'last' + str(i)
       #u.email = f'me@some{i}.com'
       #u.birthdate = datetime(2011, 1, 1)
       #u.set_password('asdf')
       #u.save()

    context = {
        jscontext('now'): datetime.now(),
    }
    return request.dmp.render('index.html', context)

