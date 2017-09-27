from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^matches/$', views.matches, name='matches'),
    url(r'^matches/(?P<match_id>\d+)/edit', views.matches_edit, name='matches_edit'),
]
