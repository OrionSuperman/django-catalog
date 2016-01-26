from django.conf.urls import patterns, url
from . import views
urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^create/$', views.create, name='cat-create'),
  url(r'^product/(?P<idx>\d+)/$', views.product),
  url(r'^update/$', views.update, name='cat-update'),
  url(r'^delete/(?P<idx>\d+)/$', views.delete),
)
