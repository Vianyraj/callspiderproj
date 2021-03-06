from django.urls import path

from . import views

from django.contrib.auth.views import LoginView,LogoutView
from questions.views import PostTemplateView, post_json
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[

     path('',LoginView.as_view(),name="login_url"),#login and authentication
     path('register/',views.registerView,name="register_url"),
     path('logout/',LogoutView.as_view(next_page='login_url'),name="logout"),

     path('dashboard/',views.get_Call_for_Proposals, name="dashboard"),#views function
     path('Call_for_Proposals_Search_Result/', views.Search_Call_for_Proposals, name="Call_for_Proposals_Search_Result"),
     path('Call_for_Papers/', views.get_Call_for_Papers, name="Call_for_Papers"),
     path('Call_for_Papers_Search_Result/', views.Search_Call_for_Papers, name="Call_for_Papers_Search_Result"),


     path('bmbfjson/', views.bmbfjson.as_view(), name="bmbfjson"),#for json
     path('wikijson/', views.Wikijson.as_view(), name="wikijson"),


]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)