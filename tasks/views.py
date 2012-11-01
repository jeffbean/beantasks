from django.shortcuts import render_to_response
from tasks.models import Task
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.contrib.auth.views import logout
from django.http import HttpResponseRedirect
from django.template.context import RequestContext

@login_required
def home(request):
    c = {}
    c.update(csrf(request))
    task_list = Task.objects.filter(doer=request.user)
    c['task_list'] = task_list
    return render_to_response('task_index.html', c, context_instance=RequestContext(request))

def bootstrap(request):
    return render_to_response('bootstrap.html', context_instance=RequestContext(request))

"""
@login_required
def add_task(request, form_class=AddTaskForm, template_name='add_task.html'):
    task_form = form_class(request.POST or None, request.user)
    if task_form.is_valid():
        Task.objects.create(user=request.user)

    else:
        "" if not posting give empty form for new task ""
        render_to_response('add_task.html', {'form': form }, context_instance=RequestContext(request))
    return render_to_response('add_task.html')
"""
def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')
