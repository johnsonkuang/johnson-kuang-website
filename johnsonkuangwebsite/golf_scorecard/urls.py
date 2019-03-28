from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.urls import path
from .views import *
app_name='golf'
urlpatterns = [
    url(r'^$', init_game, name='init_game'),
    url(r'^players/', control_player, name='control_players'),
    url(r'^players-list/$', control_player_list, name='control_players_list'),
    url(r'^player-detail/(?P<pk>\d+)/$', control_player_detail, name='control_players_detail'),
    url(r'^player-edit/(?P<pk>\d+)/$', control_person_edit, name='control_players_edit'),
    url(r'^player-delete/(?P<pk>\d+)/$', control_player_delete, name='control_players_delete'),
    url(r'^holes/$', holes, name='holes'),
    url(r'^player-selection/', choose_players, name='player_selection'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)