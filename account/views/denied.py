from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from django.contrib.auth import logout



@view_function
def process_request(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/account/login/')

    context={
        
    }
    
    return request.dmp.render('denied.html', context)
    
