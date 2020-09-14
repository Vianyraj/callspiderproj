from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpRequest
# Create your views here.
from .models import paperscrapying
import operator
#from .models import TheodoTeam



# def list_todo_items(request):
#     context={'todo_list': paperscrapying.objects.all()}
#     print(context)
#     some_list = ['1', 'B', '3', 'D', '5', 'F']
#     print('-----------------------')
#     x= operator.itemgetter(context)
#     print(x)
#     return render(request,'list.html',context)


# def add(request):
#     val1= int(request.POST['num1'])
#     val2 = int(request.POST['num2'])
#     res=val1+val2
#     return render(request,'result.html',{'result':res})

def list_todo_items(request):
    context={'todo_list': paperscrapying.objects.all()}
    return render(request,'list.html',context)
    print(context)
#
#
# def list(request):
#     return render(request,'list.html',{'name':'list'})

# def insert_todo_item(request:HttpRequest):
#     todo=paperscrapying(eventlink=request.POST['content'])
#     todo.save()
#     todo1 = paperscrapying(eventname=request.POST['content1'])
#     todo1.save()
#    # todo = paperscrapying(eventlink=)
#     #todo.save()
#     # google = paperscrapy1(movie2='google')
#     # google.save()
#
#     return redirect('list')






