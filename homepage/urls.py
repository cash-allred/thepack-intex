try:
    from django.conf.urls import url
except ImportError:
    # This is ugly, but just for backwards compatibility
    from django.urls import path as url


from . import conf

urlpatterns = [

]

from .views import overdose_deaths

urlpatterns += [
    # overdose_deaths
    url(
        '^overdosedeaths/$',
        overdose_deaths.List.as_view(),
        name=conf.OVERDOSEDEATHS_LIST_URL_NAME
    ),
    url(
        '^overdosedeaths/create/$',
        overdose_deaths.Create.as_view(),
        name=conf.OVERDOSEDEATHS_CREATE_URL_NAME
    ),
    url(
        '^overdosedeaths/(?P<pk>\d+)/$',
        overdose_deaths.Detail.as_view(),
        name=conf.OVERDOSEDEATHS_DETAIL_URL_NAME
    ),
    url(
        '^overdosedeaths/(?P<pk>\d+)/update/$',
        overdose_deaths.Update.as_view(),
        name=conf.OVERDOSEDEATHS_UPDATE_URL_NAME
    ),
    url(
        '^overdosedeaths/(?P<pk>\d+)/delete/$',
        overdose_deaths.Delete.as_view(),
        name=conf.OVERDOSEDEATHS_DELETE_URL_NAME
    ),
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

from .views import drug

urlpatterns += [
    # drug
    url(
        '^drug/$',
        drug.List.as_view(),
        name=conf.DRUG_LIST_URL_NAME
    ),
    url(
        '^drug/create/$',
        drug.Create.as_view(),
        name=conf.DRUG_CREATE_URL_NAME
    ),
    url(
        '^drug/(?P<pk>\d+)/$',
        drug.Detail.as_view(),
        name=conf.DRUG_DETAIL_URL_NAME
    ),
    url(
        '^drug/(?P<pk>\d+)/update/$',
        drug.Update.as_view(),
        name=conf.DRUG_UPDATE_URL_NAME
    ),
    url(
        '^drug/(?P<pk>\d+)/delete/$',
        drug.Delete.as_view(),
        name=conf.DRUG_DELETE_URL_NAME
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

