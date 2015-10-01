from django.conf.urls import url

from . import views

urlpatterns = [
    #login page
    url(r'^$|login/$', views.login_view, name='login'),

    url(r'^logout/$', views.logout_view, name='logout'),

    url(r'^feed/$', views.index, name='index'),

    url(r'^profile/$', views.profile, name='profile'),

    url(r'^bunk/$', views.bunk, name='bunk'),
]
