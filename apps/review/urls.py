from django.conf.urls import patterns, url
from . import views
urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^create/$', views.create),
  url(r'^product/(?P<idx>\d+)/$', views.product)
)
