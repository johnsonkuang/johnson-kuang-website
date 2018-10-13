"""
Definition of urls for johnsonkuangwebsite.
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
  url(r'^blog/', include('blog.urls',
                         namespace='blog')),
    url(r'', include('website.urls'), name='website'),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
