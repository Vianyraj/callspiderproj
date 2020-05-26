from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpRequest
# Create your views here.
from .models import paperscrapying



def list_todo_items(request):
    context={'todo_list': paperscrapying.objects.all()}
    return render(request,'list.html',context)







