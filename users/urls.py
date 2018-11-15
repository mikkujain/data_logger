from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^$', auth_views.login, {'template_name': 'auth/login.html', 'redirect_authenticated_user': True}, name='homepage'),
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name="logout"),
    url(r'^dashboard/$', views.Dashboard.as_view(), name="dashboard"),
    url(r'^page/(?P<start_date>[0-9]{4}-?[0-9]{2}-?[0-9]{2})/(?P<end_date>[0-9]{4}-?[0-9]{2}-?[0-9]{2})/$', views.Pages.as_view(), name='pages')
]