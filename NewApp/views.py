from django.shortcuts import render,redirect
from re import template
from multiprocessing import context
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from xml.dom.minidom import Identified

from django.contrib import messages
from .models import addcategory


from django.urls import reverse

# Create your views here.
def home(request):
    return render(request,'adminlogin.html',{'name':'ADCET'})

def adminlogin(request):
    return render(request, 'adminlogin.html')


def dologin(request):
    global username,password
    if request.method == 'POST':
        print("here")
        username = request.POST['username']
        password = request.POST['password']
    # user_type = request.GET.get('user_type')
      
        # user  = messages.info(request,username)
        # passs = messages.info(request,password)

    if not (username and password ):
             messages.error(request, "Please provide all fields data")
             return render(request, 'adminlogin.html')
 
    if not (username):
              messages.error(request,"Please Provide all fields data")
              return render(request,'adminlogin.html')

    if not (password):
               messages.error(request,"Please provide all fields data")
               return render(request,'adminlogin.html')
    
    if username != 'admin' and password != 'admin' :
        messages.error(request,'fill correct data')
        return render(request,'adminlogin.html')

    if username == 'admin' and password == 'admin' :
        messages.success(request,'succesfully')
        return render(request,'admindashboard.html')

    
    else:
        return render(request, 'adminlogin.html')



def admindashboard(request):
    return render(request,'admindashboard.html')

def addCategory(request):
    if request.method == 'POST':
        Category = request.POST['category']
        print(Category)
        addCategory_data=addcategory(category=Category)
        addCategory_data.save()
        messages.success(request,"Product Category Submitted")
    return render(request,'addcategory.html')

#view Category data
def viewcategorydata(request):
    category_info = addcategory.objects.all().values()
    print(category_info,type(category_info))
    context = {
        "category_info" : category_info,
        }  
    return render(request,"categoryView.html",context)  

def delete_category(request,id):
    delete_contact = addcategory.objects.get(id=id)
    print("ID",id)
    delete_contact.delete()
    messages.error(request , "branch deleted")
    return redirect("viewcategorydata")

def update(request, id):
  mymember = addcategory.objects.get(id=id)
  template = loader.get_template('updatecategory.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request,id):
    category = request.POST['category']

    member = addcategory.objects.get(id=id)
    member.category = category
  
    member.save()
    messages.success(request,"Product Category Updated")
    return HttpResponseRedirect(reverse('viewcategorydata'))

# def updatecategory(request):
#     return render(request,'updatecategory.html')