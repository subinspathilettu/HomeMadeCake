from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^cake/(?P<pk>\d+)/$', views.cake_details, name='cake_details'),
    url(r'^cake/new/$', views.cake_new, name='cake_new'),
    url(r'^login/$', views.vendor_login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^accounts/profile/$',  views.profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)