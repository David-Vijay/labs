from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    path('', views.register, name='register'),
    path('login',views.log, name='login'),
    path('lgout',views.log_out, name='logout'),
    path('home',views.home,name='home'),
    path('user',views.userPage, name='user'),
    path('appdata',views.appData, name='appdata'),
    path('appdata/<int:app_Id>', views.appData, name='appdata')
]