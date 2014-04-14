from django.conf.urls import patterns, url
from dashboard import views

urlpatterns = patterns('', 
    # ex: /polls/
    url(r'^', views.dashboard, name='dashboard'),
    # ex: /polls/5/
    # Note: ?P<poll_id> is the name that the match will be captured as
    #url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    )