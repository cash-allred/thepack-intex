try:
    from django.conf.urls import url
except ImportError:
    # This is ugly, but just for backwards compatibility
    from django.urls import path as url


urlpatterns = [

]
