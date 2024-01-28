from django.urls import re_path, include, path

from accounts import views
from accounts.views import activation, send_email_view

# from accounts.views import activation, send_email_view

urlpatterns = [
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
    re_path(r'^auth/', include('djoser.social.urls')),
    path('api-auth/', include('rest_framework.urls')),
    # path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',views.activate, name='activate')
    path('activate/<str:uid>/<str:token>/', activation, name='activation'),
    path('send-email/', send_email_view, name='send_email'),
]
# bc1466d4345a203c160aea4958a8522b