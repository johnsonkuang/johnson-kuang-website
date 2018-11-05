from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.urls import path
from website.views import control_newsletter, control_newsletter_list, control_newsletter_detail, control_newsletter_edit, control_newsletter_delete

urlpatterns = [
    url(r'^newsletter/$', control_newsletter, name='control_newsletter'),
    url(r'^newsletter-list/$', control_newsletter_list, name='control_newsletter_list'),
    url(r'^newsletter-detail/(?P<pk>\d+)/$', control_newsletter_detail, name='control_newsletter_detail'),
    url(r'^newsletter-edit/(?P<pk>\d+)/$', control_newsletter_edit, name='control_newsletter_edit'),
    url(r'^newsletter-delete/(?P<pk>\d+)/$', control_newsletter_delete, name='control_newsletter_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)