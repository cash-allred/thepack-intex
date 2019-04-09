from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
try:
    from django.core.urlresolvers import reverse_lazy
except ImportError:
    from django.urls import reverse_lazy
from django import http


from base import views as base_views

from .. import (
    models,
    forms,
    conf
)


class List(LoginRequiredMixin, base_views.BaseListView):
    """
    List all Drugs
    """
    queryset = models.Drug.objects.all()

    def __init__(self):
        super(List, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)

        context['detail_url_name'] = conf.DRUG_DETAIL_URL_NAME

        if self.request.user.has_perm("homepage.add_drug"):
            context['create_object_reversed_url'] = reverse_lazy(
                conf.DRUG_CREATE_URL_NAME
            )
        
        return context


class Create(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseCreateView):
    """
    Create a Drug
    """
    model = models.Drug
    permission_required = (
        'homepage.add_drug'
    )
    form_class = forms.Drug

    def __init__(self):
        super(Create, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.DRUG_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())


class Detail(LoginRequiredMixin, base_views.BaseDetailView):
    """
    Detail of a Drug
    """
    model = models.Drug

    def __init__(self):
        super(Detail, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)

        if self.request.user.has_perm("homepage.change_drug"):
            context['update_object_reversed_url'] = reverse_lazy(
                conf.DRUG_UPDATE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )

        if self.request.user.has_perm("homepage.delete_drug"):
            context['delete_object_reversed_url'] = reverse_lazy(
                conf.DRUG_DELETE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )

        return context


class Update(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseUpdateView):
    """
    Update a Drug
    """
    model = models.Drug
    form_class = forms.Drug
    permission_required = (
        'homepage.change_drug'
    )

    def __init__(self):
        super(Update, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.DRUG_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())


class Delete(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseDeleteView):
    """
    Delete a Drug
    """
    model = models.Drug
    permission_required = (
        'homepage.delete_drug'
    )

    def __init__(self):
        super(Delete, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.DRUG_LIST_URL_NAME)
