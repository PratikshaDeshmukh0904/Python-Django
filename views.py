from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
# from .models import  AdminHOD,auth

# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'ADCET'})

     
def registration(request):
    return render(request, 'registration.html')
     
def adminlogin(request):
    return render(request, 'adminlogin.html')


# def doLogin(request):
#     if request.method=='POST':
#        username = request.POST['username']
#         password = request.POST['password']

#       user = auth.authenticate(username=='admin' ,password=='admin')

#       if AdminHOD is not None:
#         auth.doLogin(request,user)
#         return redirect("/")
        
#         else:
#             messages.info(request,'invalid credentials')
#             return render(request,'adminlogin.html')

       