from django.urls import path

from .import views

urlpatterns = [
path('',views.home,name='home'),
path('registration', views.registration, name="registration"),
path('adminlogin',views.adminlogin,name="adminlogin"),

]