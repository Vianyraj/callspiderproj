

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View,ListView
from rest_framework import generics

from rest_framework.generics import ListAPIView

from .forms import UserForm
from django.http import HttpResponse,HttpRequest
from django.contrib.auth.forms import UserCreationForm
from .models import Paper_model

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control#for again not letting the user to enter into session when
                                                       #back button is pressed


from rest_framework.views import APIView
from .serializers import PaperSerializer
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

#filters.py
from .filters import OrderFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters





def list_events(request,pk_test):#definition to display the last 40 values of the database
    context={}
    filter_backends=(DjangoFilterBackend,)

    list_events= Paper_model.objects.get(id=pk_test)
    orders= list_events.order_set.all()
    Title=Paper_model.objects.all
    Dates= Paper_model.objects.all
    myFilter = OrderFilter(request.GET,queryset=list_events)
    orders= myFilter
    #context= {'myFilter' : myFilter}
    context = {'Title':Title,'Dates':Dates, 'myFilter': myFilter}
    #context= {'list_events': Paper_model.objects.order_by('-id')[:40], 'myFilter':myFilter.qs}

    return render(request,'dashboard.html',context)







def indexView(request):
    return render(request,'index.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login_url')

# def dashboardView(request):
#     myFilter = OrderFilter()
#     context={'list_events': Paper_model.objects.order_by('-id')[:40]}
#
#     return render(request, 'dashboard.html', context)
#     #return render(request,'dashboard.html')
# # for list html <a href="http://127.0.0.1:8000/list/">To paper list</a>


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



class PaperList(generics.ListAPIView):#display the database data on the webpage
    serializer_class = PaperSerializer
    def get_queryset(self):
        queryset=Paper_model.objects.all()

        # active= self.request.query_params.get('PaperType','')
        # if active:
        #     if active == "Wiki":
        #         active="Wiki"
        #         print("wiki")
        #         print("------------------------------------------")
        #     elif active=="Bmbf":
        #         active= "Bmbf"
        #         print("wiki---------------------------------")
        #     else:
        #         return queryset
        #     return queryset.filter(PaperType=active)

        # serializer_class = PaperSerializer(queryset, many=True)
        # filter_backends = [filters.SearchFilter]
        search_fields = ['Title', 'PaperType','Where']
        # #filter_backends = (DjangoFilterBackend,SearchFilter,  OrderingFilter)
        # ##filter_backends = (SearchFilter, OrderingFilter)
        # filter_fields = ('Title','PaperType',)
        # #return Response(serializer_class.data)
        return queryset

class SnippetListView(ListView):
    model = Paper_model
    template_name = 'questions/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter']= OrderFilter(self.request.GET, queryset= self.get_queryset())
        print(context)
        print("-000000000000000000000000")
        return render( 'dashboard.html', context)


    def dashboardView(request):
        myFilter = OrderFilter()
        context = {'list_events': Paper_model.objects.order_by('-id')[:40]}

        return render(request, 'dashboard.html', context)
        # return render(request,'dashboard.html')


# class SnippetListView(ListView):
#     model = Paper_model
#     template_name = 'templates/dashboard.html'
# def dashboardView(request):
#     myFilter = OrderFilter()
#     context={'list_events': Paper_model.objects.order_by('-id')[:40]}
#
#     return render(request, 'dashboard.html', context)
#     #return render(request,'dashboard.html')
# # for list html <a href="http://127.0.0.1:8000/list/">To paper list</a>
