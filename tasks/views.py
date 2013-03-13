# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from tasks.models import Task, Object;
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from random import randrange;

def index(request):
	# get the first task
	#task_id = randrange(3500);
	task_id = 1;
	#task = Task.objects.get(id=task_id);
	#template = loader.get_template('tasks/task.html');
	#context = {'task': task};
	#return render(request, 'tasks/task.html', context);
	return HttpResponseRedirect(reverse('tasks:task', args=(task_id,)))

def task(request, task_id):
	# get the first task
	#task_id = randrange(3500);
	task = Task.objects.get(id=task_id);
	template = loader.get_template('tasks/task.html');
	context = {'task': task};
	return render(request, 'tasks/task.html', context);

def results(request, task_id):
	#return HttpResponse("You are looking at the results of task %s"%(task_id));
	task = get_object_or_404(Task, id=task_id);
	context = {'task': task};
	return render(request, 'tasks/results.html', context);

def vote(request, task_id):
	#return HttpResponse("You are looking at the results of task %s"%(task_id));
	t = get_object_or_404(Task, id=task_id);
	#selected_choice = t.question.choice_set.get(id=request.POST['choice'])
	#selected_choice.votes += 1;
	#selected_choice.save();
	# do something, and then load the next task
	next_id = randrange(3350);
	task = Task.objects.get(id=next_id);
	#template = loader.get_template('tasks/task.html');
	#context = {'task': task};
	#return render(request, 'tasks/task.html', context);
	return HttpResponseRedirect(reverse('tasks:task', args=(next_id,)))

def test(request):
	# get the first task
	task = Task.objects.get(id=1);
	template = loader.get_template('tasks/test.html');
	context = {'task': task};
	return render(request, 'tasks/test.html', context);
