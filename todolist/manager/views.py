from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from django import forms
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse

# Create your views here.

def index(request): 
    print request.user
    if request.user.is_authenticated():
        return redirect("/admin/")
    else:
        url = reverse('django.contrib.auth.views.login')
        return redirect(url, template_name='login.html')
        return HttpResponse("zzzz")



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.is_staff = True
            new_user.save()
            ps = Permission.objects.filter(codename__endswith='_todoitem')
            new_user.user_permissions = ps
            return HttpResponseRedirect("/admin")
    else:
        form = UserCreationForm()
    data = {'form': form}
    data.update(csrf(request))
    return render_to_response("register.html", data)
