from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.loginpage,name='login' ),
    path('edit/<int:id>/',views.edit,name='edit' ),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('login/', views.loginpage, name='login'),
    path('signup/', views.registerpage, name='signup'),
    path('logout/', views.logoutUser, name='logout'),
    path('index/', views.index, name='index'),
    path('history/', views.tryd, name='history'),
    path('statistics/', views.try1, name='statistics'),
]
