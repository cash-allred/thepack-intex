from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime
from django.http import *

@view_function
def process_request(request):
    # did the user submit?
    if request.method == "POST":
        # check all of the variables
        # assume the user did it wrong
        print(">>>>>>>" + request.POST['yourname'])
        # if the user did it right
        # do the work
        
    context = {
        
    }
    return request.dmp.render('contact.html', context)
