from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as hmod
import math

ITEMS_PER_PAGE = 8

@view_function
def process_request(request):
    doctors = hmod.Doctor.objects.all()

    #numpages = math.ceil(doctors.count()/ ITEMS_PER_PAGE)
    #doctors = doctors[(page-1) * ITEMS_PER_PAGE: page * ITEMS_PER_PAGE]
     
    context={
        'doctors': doctors,
        #'page': page,
        #'numpages': numpages,
    }
    return request.dmp.render('index.html', context)