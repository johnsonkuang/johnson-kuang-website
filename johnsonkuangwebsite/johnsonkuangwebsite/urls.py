"""
Definition of urls for johnsonkuangwebsite.
"""

from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from website import views

from website.sitemaps import *
admin.autodiscover()

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'', include('website.urls'), name='website'),
    url(r'^science-olympiad/resources', views.science_olympiad_resources, name='science-olympiad-resources'),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^control/', include(('control_panel.urls', 'control_panel'), namespace='control_panel')),
    url(r'^accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
