from django.conf.urls import url
from . import views
from rest_framework.authtoken import views as view

urlpatterns = [
    # ADMIN PRIVILEGES
    url(r'^$', views.ProfileList.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'users/add/$', views.AddUser.as_view()),
    url(r'add/$', views.AddProfile.as_view()),
    url(r'self/$', views.SelfDetails.as_view()),
    url(r'^token-auth/$', view.obtain_auth_token),
]
