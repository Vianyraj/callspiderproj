

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth import logout
from django.http import HttpResponse,HttpRequest
from django.contrib.auth.decorators import login_required
#from .models import Questions
from django.contrib.auth.forms import UserCreationForm
from .models import Paper_model

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control#for again not letting the user to enter into session when
                                                       #back button is pressed

def list_events(request):#definition to display the last 40 values of the database

    context={'list_events': Paper_model.objects.order_by('-id')[:40]}
    print(context)
    return render(request,'list.html',context)#







def indexView(request):
    return render(request,'index.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login_url')

def dashboardView(request):
    context={'list_events': Paper_model.objects.order_by('-id')[:40]}
    return render(request, 'dashboard.html', context)
    #return render(request,'dashboard.html')
# for list html <a href="http://127.0.0.1:8000/list/">To paper list</a>


def registerView(request):
    form = "Dummy String"
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form=UserCreationForm()

    return render(request,'registration/register.html',{'form':form})







def LogoutView(request):
    logout(request)
    #return redirect('/login')
    # Redirect to a success page.








class UserFormView(View):
    form_class = UserForm
    template_name='questions/registration_form.html'
