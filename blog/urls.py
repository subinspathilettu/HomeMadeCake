from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^cake/(?P<pk>\d+)/$', views.cake_details, name='cake_details'),
]