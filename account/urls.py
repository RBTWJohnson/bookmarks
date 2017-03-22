from django.conf.urls import url
from . import views


urlpatterns = [
    # original login
    url(r'^login/$', views.user_login, name='login'),
    # login logout via django
    url(r'^login/$', 'django.congtrib.auth.views.login',name = 'login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name = 'logout'),
    url(r'^logout-then-login/$','django.contrib.auth.views.logout_then_login', name = 'logout_then_login'),
    url(r'^$', views.dashboard, name = 'dashboard')

]