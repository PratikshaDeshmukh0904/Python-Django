from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Admin
from .models import branch
from .models import StandardMaster
# from .models import  AdminHOD,auth
#from django.contrib.auth import auth,dologin,user

# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'ADCET'})

def registration(request):
    return render(request, 'registration.html')

def adminlogin(request):
    return render(request, 'adminlogin.html')

def studentlogin(request):
    return render(request,'studentlogin.html')

def stafflogin(request):
    return render(request,'stafflogin.html')


def dologin(request):
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
    return render(request,"admindashboard.html")
    
def branchmaster(request):
    if request.method =="POST":
        id = request.POST["id"]
        branch_name = request.POST["branchname"]
        
        branch_data = branch(id=id,branch_name=branch_name)
        print(id,branch_name)
        branch_data.save()
        messages.success(request,'Successfully added')
        return render(request,'branchmaster.html')

    if request.method == "POST":
            id == '' 
            branch_name == ''
            messages.error(request,"Please Provide all fields data")
            return render(request,'branchmaster.html')
    else:
           return render(request,'branchmaster.html')

    
def viewbranchdata(request):
             branch_info = branch.objects.all()
             print(branch_info)
             context = {
                 "branch_info" : branch_info,
                  }  
             return render(request,"Viewbranch.html",context)     

    

def standard(request):
    if request.method == "POST":
        SrNumber = request.POST["SrNO"]
        standardname = request.POST["standardname"]

        standard_data = StandardMaster(SrNumber=SrNumber,standardname=standardname)
        print(SrNumber,standardname)
        standard_data.save()
        messages.success(request,'Successfully Added')
        return render(request,'standard.html')

    if request.method == "POST":
        SrNumber == ''
        standardname == ''
        messages.error(request,'Please provide all data...!')
        return render(request,'standard.html')

    else:
        return render(request,'standard.html')


def staffregister(request):
        return render(request,'staffregistration.html')