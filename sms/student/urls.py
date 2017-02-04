from django.conf.urls import url
from . import views

app_name = 'student'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^index/$', views.index, name='index'),
    # url(r'^', views.login_user, name='login_user'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),

]