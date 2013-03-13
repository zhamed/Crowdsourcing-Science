from django.conf.urls import patterns, url

from tasks import views

urlpatterns = patterns('',
	# /tasks/
	url(r'^$', views.index, name='index'),
	# /tasks/1/results/
	url(r'^(?P<task_id>\d+)/results/$', views.results, name='results'),
	url(r'^(?P<task_id>\d+)/vote/$', views.vote, name='vote'),
	url(r'^(?P<task_id>\d+)/task/$', views.task, name='task'),
        # /tasks/test
	url(r'^test/$', views.test, name='test'),
                       
)
