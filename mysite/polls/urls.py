#Author:xubojoy

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),#name指定指向的HTML   之后URL可以随便写
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$',views.ResultsView.as_view(),name='results'),
    url(r'^(?P<question_id>[0-9]+)/vo/$',views.vote,name='vote'),
    # url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
    # url(r'^(?P<question_id>[0-9]+)/results/$',views.results,name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
]