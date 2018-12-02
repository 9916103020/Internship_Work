from django.shortcuts import render,HttpResponseRedirect, HttpResponse
from .forms import RegistrationForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url="login")
def profile(request):
    args= {'user': request.user}
    return render(request, 'editor2.html')

def login(request):
    return render(request,'login.html')
	
	
	
@login_required(login_url="login")
def logout(request):
    return render(request,'logout.html')

def choice(request):
    return render(request,'accounts/choice.html')

def register(request):
     if request.method == 'POST':
         form = RegistrationForm(request.POST)
         if form.is_valid():
             form.save()
             return render(request,'accounts/choice.html')
             # return HttpResponseRedirect('/choice/')
         else:
             return HttpResponseRedirect('/error/')
     else:
         form= RegistrationForm(request.POST)

         args = {'form': form}
         return render(request, 'accounts/reg_form.html',args)
