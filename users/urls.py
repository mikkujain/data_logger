from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^$', auth_views.login, {'template_name': 'auth/login.html', 'redirect_authenticated_user': True}, name='homepage'),
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name="logout"),
    url(r'^dashboard/$', views.Dashboard, name="dashboard"),
]