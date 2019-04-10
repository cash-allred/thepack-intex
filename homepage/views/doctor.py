from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
try:
    from django.core.urlresolvers import reverse_lazy
except ImportError:
    from django.urls import reverse_lazy
from django import http
from django_mako_plus import view_function, jscontext
from datetime import datetime
from homepage import models as hmod


from base import views as base_views

from .. import (
    models,
    forms,
    conf
)

#CREATE
#READ: reading and searching capability is taken care of with the @view_function process request
#UPDATE
#DELETE


#figure out create function!
@view_function
def process_request(request):
    form = doctorCreateForm()
    hmod.Doctor.objects.add_doctor()
        
    context = {
        'doctors': doctors,
        'form': form,
        jscontext('now'): datetime.now(),
    }
    return request.dmp.render('doctor.html', context)

class List(LoginRequiredMixin, base_views.BaseListView):
    """
    List all Doctors
    """
    queryset = models.Doctor.objects.all()

    def __init__(self):
        super(List, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)

        context['detail_url_name'] = conf.DOCTOR_DETAIL_URL_NAME

        if self.request.user.has_perm("homepage.add_doctor"):
            context['create_object_reversed_url'] = reverse_lazy(
                conf.DOCTOR_CREATE_URL_NAME
            )
        
        return context


class Create(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseCreateView):
    """
    Create a Doctor
    """
    model = models.Doctor
    permission_required = ('homepage.add_doctor')
    form_class = forms.Doctor

    def __init__(self):
        super(Create, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.DOCTOR_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())


class Detail(LoginRequiredMixin, base_views.BaseDetailView):
    """
    Detail of a Doctor
    """
    model = models.Doctor

    def __init__(self):
        super(Detail, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)

        if self.request.user.has_perm("homepage.change_doctor"):
            context['update_object_reversed_url'] = reverse_lazy(
                conf.DOCTOR_UPDATE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )

        if self.request.user.has_perm("homepage.delete_doctor"):
            context['delete_object_reversed_url'] = reverse_lazy(
                conf.DOCTOR_DELETE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )

        return context


class Update(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseUpdateView):
    """
    Update a Doctor
    """
    model = models.Doctor
    form_class = forms.Doctor
    permission_required = ('homepage.change_doctor')

    def __init__(self):
        super(Update, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.DOCTOR_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())


class Delete(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseDeleteView):
    """
    Delete a Doctor
    """
    model = models.Doctor
    permission_required = ('homepage.delete_doctor')

    def __init__(self):
        super(Delete, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.DOCTOR_LIST_URL_NAME)
