from django.conf.urls import url
from django.contrib.auth import views as auth_views

from accounts import views

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), {'next_page': 'accounts:login'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/edit$', views.profile, name='profile_edit'),
]
