try:
    from django.conf.urls import url
except ImportError:
    # This is ugly, but just for backwards compatibility
    from django.urls import path as url


from . import conf

urlpatterns = [

]

from .views import prescription

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


from .views import doctor

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

