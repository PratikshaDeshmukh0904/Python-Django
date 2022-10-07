from django.shortcuts import render ,HttpResponse , redirect 
from home.models import Contact
from django.contrib import messages
from django.core.paginator import Paginator , EmptyPage ,PageNotAnInteger

# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        dateofbirth = request.POST["dob"]

        contact_data = Contact(name=name , email=email , mobile=mobile , dateofbirth=dateofbirth)
        contact_data.save()
        messages.success(request , "Contact Saved")
        return redirect("home")

    contact_list = Contact.objects.all()
    
    context = {
    'contact_data' : contact_list ,
    
    }
    return render(request , "index.html" , context)

def edit_contact(request , sno):
    context = {
    'edit_contact' : Contact.objects.get(sno=sno)
    }
    return render(request , "edit_contact.html" , context)

def update(request , sno):
    contact = Contact.objects.get(sno=sno)
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        dateofbirth = request.POST["dob"]

        contact_data = Contact(name=name , email=email , mobile=mobile , dateofbirth=dateofbirth)
        contact_data.save()
        messages.success(request , "Contact Updated")
        return redirect("home")
    
    return render(request , "edit_contact.html" , {contact})

def delete_contact(request , sno):
    delete_contact = Contact.objects.get(sno=sno)
    delete_contact.delete()
    messages.error(request , "Contact delated")
    return redirect("home")
 
def search(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        dateofbirth = request.POST["dob"]

        contact_data = Contact(name=name , email=email , mobile=mobile , dateofbirth=dateofbirth)
        contact_data.save()
        messages.success(request , "Contact Saved")
        return redirect("home")
    query = request.GET["query"]
    search_name = Contact.objects.filter(name__icontains=query)
    search_email = Contact.objects.filter(email__icontains=query)
    search_mobile = Contact.objects.filter(mobile__icontains=query)
    search_data = search_name.union(search_email , search_mobile)
    if search_data.count() ==0 :
        messages.error(request , "Search Not available")
    context = {
        "contact_data": search_data ,
        "query": query ,
    } 
    
    return render (request , "search.html", context)


