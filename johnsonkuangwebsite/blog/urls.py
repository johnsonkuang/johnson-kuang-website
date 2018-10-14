from django.conf.urls import url
from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/',
            views.post_list, name='post_list_by_tag'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
    url(r'^(?P<post_id>\d+)/share/$', views.post_share,
        name='post_share'),
]
