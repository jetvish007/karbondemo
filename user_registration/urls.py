from django.conf.urls import url
from user_registration import views
from django.urls import path


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'register/$', views.register, name='register'),
    url(r'user_login/$', views.user_login, name='user_login'),
    url(r'user_logout/$', views.user_logout, name='user_logout'),
    url(r'^welcome/$', views.welcome, name='welcome'),
]
