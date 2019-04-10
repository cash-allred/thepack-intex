"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from homepage import conf 

urlpatterns = [
    # the built-in Django administrator
    url('admin/', admin.site.urls),
    #path('account/', include('django.contrib.auth.urls')),

    # urls for any third-party apps go here

    # the DMP router - this should normally be the last URL listed
    url('', include('django_mako_plus.urls')),
]

from homepage.views import prescription

urlpatterns += [
    # prescription
    url(
        '^prescription/$',
        prescription.List.as_view(),
        name=conf.PRESCRIPTION_LIST_URL_NAME
    ),
    url(
        '^prescription/create/$',
        prescription.Create.as_view(),
        name=conf.PRESCRIPTION_CREATE_URL_NAME
    ),
    url(
        '^prescription/(?P<pk>\d+)/$',
        prescription.Detail.as_view(),
        name=conf.PRESCRIPTION_DETAIL_URL_NAME
    ),
    url(
        '^prescription/(?P<pk>\d+)/update/$',
        prescription.Update.as_view(),
        name=conf.PRESCRIPTION_UPDATE_URL_NAME
    ),
    url(
        '^prescription/(?P<pk>\d+)/delete/$',
        prescription.Delete.as_view(),
        name=conf.PRESCRIPTION_DELETE_URL_NAME
    ),
]

from homepage.views import doctor

urlpatterns += [
    # doctor
    url(
        '^doctor/$',
        doctor.List.as_view(),
        name=conf.DOCTOR_LIST_URL_NAME
    ),
    url(
        '^doctor/create/$',
        doctor.Create.as_view(),
        name=conf.DOCTOR_CREATE_URL_NAME
    ),
    url(
        '^doctor/(?P<pk>\d+)/$',
        doctor.Detail.as_view(),
        name=conf.DOCTOR_DETAIL_URL_NAME
    ),
    url(
        '^doctor/(?P<pk>\d+)/update/$',
        doctor.Update.as_view(),
        name=conf.DOCTOR_UPDATE_URL_NAME
    ),
    url(
        '^doctor/(?P<pk>\d+)/delete/$',
        doctor.Delete.as_view(),
        name=conf.DOCTOR_DELETE_URL_NAME
    ),
]