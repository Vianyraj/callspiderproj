from django.urls import path

from . import views

urlpatterns=[
    path('',views.list_todo_items,name='list'),
    #path('insert_todo_item',views.insert_todo_item,name='insert_todo_item'),

]