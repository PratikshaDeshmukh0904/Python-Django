from django.shortcuts import render,redirect
from re import template
from multiprocessing import context
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from xml.dom.minidom import Identified

from django.contrib import messages
from .models import addcategory,addproduct

from django.core.files.storage import FileSystemStorage


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

#Add Products 
def  addProducts(request):
    category_info = addcategory.objects.all().values()
    print(category_info,type(category_info))
    context = {
        "category_info" : category_info,
    }    
    if request.method == 'POST' and request.FILES['upload']:
        
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        ProductName = request.POST['pname']
        ProductPrice = request.POST['pprice']
        Category = request.POST['category']
        Features = request.POST['features']
        print(Category)
        addCategory_data=addproduct(productname=ProductName,productprice=ProductPrice,category=Category,features=Features,product_Img=upload)
        addCategory_data.save()
        messages.success(request,"Product Submitted")
        return render(request, 'addproduct.html', {'file_url': file_url})
    return render(request,'addproduct.html',context)

#Product View
def viewproductdata(request):
    product_info = addproduct.objects.all().values()
    print(product_info,type(product_info))
    context = {
        "product_info" : product_info,
        }  
    return render(request,"productsview.html",context)  

#Delete Product
def delete_product(request,id):
    delete_p = addproduct.objects.get(pid=id)#database column=whatever you want
    print("ID",id)
    delete_p.delete()
    messages.error(request , "product deleted")
    return redirect("viewproductdata")


def updateproduct(request,id):
  myproducts = addproduct.objects.get(pid=id)
  template = loader.get_template('updateproducts.html')
  context = {
    'myproducts': myproducts,
  }
  return HttpResponse(template.render(context, request))

#Update Record
def updateproductrecord(request,id):
    ProductName = request.POST['pname']
    ProductPrice = request.POST['pprice']
    Category = request.POST['category']
    Features = request.POST['features']
    Image = request.POST['upload']
    member = addproduct.objects.get(pid=id)
    member.productname = ProductName
    member.productprice = ProductPrice
    member.category = Category
    member.features = Features
    member.product_Img = Image
    member.save()
    messages.success(request,"Product Updated")
    return HttpResponseRedirect(reverse('viewproductdata'))
