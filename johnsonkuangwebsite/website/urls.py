from django.conf.urls import url

from . import views


app_name = 'website'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^resume/', views.resume, name='resume'),
    url(r'^projects/', views.projects, name='projects'),
    url(r'^sandbox/', views.sandbox, name='sandbox'),
    url(r'^terms/', views.term, name='terms'),
    url(r'^newsletter/sign_up/$', views.newsletter_signup, name='newsletter_signup'),
    url(r'^newsletter/unsubscribe/$', views.newsletter_unsubscribe, name='newsletter_unsubscribe')
]
