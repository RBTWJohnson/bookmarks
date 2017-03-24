from django.conf.urls import url, include
import django.contrib.auth

from . import views


urlpatterns = [
    url(r'^$', views.dashboard, name = 'dashboard'),
    #url(r'^login/$', views.user_login, name='login'),
    url(r'^login/$' , django.contrib.auth.login, name='login'),
    url(r'^logout/$', django.contrib.auth.logout, name='logout'),
    #url(r'^logout-then-login/$', django.contrib.auth.logout_then_login, name='logout_then_login'),
    url(r'^register/$', views.register, name='register'),


]
