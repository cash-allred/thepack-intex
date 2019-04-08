from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from django.contrib.auth import logout



@view_function
def process_request(request):
    logout(request)
    # Redirect to a success page.

    return HttpResponseRedirect('/')
    
