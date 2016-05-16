from django.conf.urls import include, url

from . import views

app_name = 'connect4'
urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^signup/$', views.SignupView.as_view(), name='signup'),
    url(r'^games/$', views.GamesView.as_view(), name='games'),
    url(r'^play/(?P<game>[0-9]+)/$', views.PlayView.as_view(), name='play'),
]
