from django.urls import path
from .import views

urlpatterns = [

   
    path('', views.user_login, name="user_login"),
    path('user_register', views.user_register.as_view(), name="user_register"),
    path('user_logout', views.user_logout, name="user_logout"),
    path('registration', views.registration, name="registration"),
   
 
]