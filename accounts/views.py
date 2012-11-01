from accounts.forms import RegistrationFrom
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import logout
from accounts.models import BeanUser
from django.contrib.auth.decorators import login_required

def NewUserRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    if request.method == 'POST':
        form = RegistrationFrom(request.POST)
        if form.is_valid():
            user = User.objects.create(username=form.cleaned_data['username'],
                                       email=form.cleaned_data['email'])
            user.set_password(form.cleaned_data['password'])
            user.save()
            bean_user = BeanUser(user=user, user_image=form.cleaned_data['user_image'])
            bean_user.save()
            return HttpResponseRedirect('/profile/')
        else:
            return render_to_response('register.html', {'form':form}, context_instance=RequestContext(request))
    else:
        """ not a post so display empty registration form """
        form = RegistrationFrom()
        context = {'form': form }
        return render_to_response('register.html', context, context_instance=RequestContext(request))

@login_required
def user_home(request):
    return render_to_response('user_home.html', context_instance=RequestContext(request))

def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/login/')
