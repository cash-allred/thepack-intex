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
    List all OverdoseDeathss
    """
    queryset = models.OverdoseDeaths.objects.all()

    def __init__(self):
        super(List, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)

        context['detail_url_name'] = conf.OVERDOSEDEATHS_DETAIL_URL_NAME

        if self.request.user.has_perm("homepage.add_overdosedeaths"):
            context['create_object_reversed_url'] = reverse_lazy(
                conf.OVERDOSEDEATHS_CREATE_URL_NAME
            )
        
        return context


class Create(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseCreateView):
    """
    Create a OverdoseDeaths
    """
    model = models.OverdoseDeaths
    permission_required = (
        'homepage.add_overdosedeaths'
    )
    form_class = forms.OverdoseDeaths

    def __init__(self):
        super(Create, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.OVERDOSEDEATHS_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())


class Detail(LoginRequiredMixin, base_views.BaseDetailView):
    """
    Detail of a OverdoseDeaths
    """
    model = models.OverdoseDeaths

    def __init__(self):
        super(Detail, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)

        if self.request.user.has_perm("homepage.change_overdosedeaths"):
            context['update_object_reversed_url'] = reverse_lazy(
                conf.OVERDOSEDEATHS_UPDATE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )

        if self.request.user.has_perm("homepage.delete_overdosedeaths"):
            context['delete_object_reversed_url'] = reverse_lazy(
                conf.OVERDOSEDEATHS_DELETE_URL_NAME,
                kwargs=self.kwargs_for_reverse_url()
            )

        return context


class Update(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseUpdateView):
    """
    Update a OverdoseDeaths
    """
    model = models.OverdoseDeaths
    form_class = forms.OverdoseDeaths
    permission_required = (
        'homepage.change_overdosedeaths'
    )

    def __init__(self):
        super(Update, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.OVERDOSEDEATHS_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())


class Delete(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseDeleteView):
    """
    Delete a OverdoseDeaths
    """
    model = models.OverdoseDeaths
    permission_required = (
        'homepage.delete_overdosedeaths'
    )

    def __init__(self):
        super(Delete, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.OVERDOSEDEATHS_LIST_URL_NAME)
