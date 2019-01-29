"""urlconf for the base application"""

from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^api/v1/user/authenticate.*$', auth, name='auth'),
    url(r'^api/v1/user/licenses/?access_token=.*$', token, name='token'),
    url(r'^api/v1/user/licenses/1/register?.*$', register, name='register'),
]
