from django.urls import path

from . import views
from django.contrib.auth.views import LoginView,LogoutView
#from . import dbconnection

urlpatterns=[
     path('list/',views.list_events,name='list'),
     path('',views.indexView,name='home'),
     #path('dashboard/',views.list_events,name='dashboard'),
     path('dashboard/',views.dashboardView,name="dashboard"),
     path('login/',LoginView.as_view(),name="login_url"),
     path('register/',views.registerView,name="register_url"),
     path('logout/',LogoutView.as_view(next_page='dashboard'),name="logout"),
    #path('insert_todo_item',views.insert_todo_item,name='insert_todo_item'),

]