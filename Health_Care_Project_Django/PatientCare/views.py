from django.shortcuts import render

from re import template
from xml.dom.minidom import Identified
from django.shortcuts import render,redirect
from django.http import HttpResponse
import io
import mysql.connector as pymysql 
#For Messages
from django.contrib import messages
#Response 
from django.http import HttpResponse, HttpResponseRedirect
#Reverse
from django.urls import reverse
#Loader
from django.template import loader
#Import Models
from .models import admin,addcategory

# Create your views here.

#Home Page 
def home(request):
    return render(request,'home.html')

#To open Admin_Login Page
def adminlogin(request):
    return render(request, 'adminlogin.html')


#After submit data of admin
def dologin(request):
    global user,passw
    if request.method =='POST':
        m=pymysql.connect(host="localhost",user="root",password="",database="healthcare")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="username":
                user=value
            if key=="password":
                passw=value
           
        
        c="select * from admin where User='{}' and Pass='{}'".format(user,passw)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'adminlogin.html')
        else:
            return render(request,"admindashboard.html")
    
    return render(request,'adminlogin.html')

#AdminDashboard
def admindashboard(request):
    return render(request,"admindashboard.html")

    
#Add Category
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

#Delete Category
def delete_category(request,id):
    delete_contact = addcategory.objects.get(id=id)
    print("ID",id)
    delete_contact.delete()
    messages.error(request , "category deleted")
    return redirect("viewcategorydata")

def update(request, id):
  mymember = addcategory.objects.get(id=id)
  template = loader.get_template('updatecategory.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

#Update Record
def updaterecord(request,id):
    category = request.POST['category']
    member = addcategory.objects.get(id=id)
    member.category = category
    member.save()
    messages.success(request,"Product Category Updated")
    return HttpResponseRedirect(reverse('viewcategorydata'))
