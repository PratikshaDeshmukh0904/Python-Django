from django.urls import path
from .import views


urlpatterns = [
    path('',views.home,name='home'),
    path('adminlogin',views.adminlogin,name="adminlogin"),
    path('dologin',views.dologin,name="dologin"),
    path('admindashboard',views.admindashboard,name="admindashboard"),
    path('addCategory',views.addCategory,name="addCategory"),
    path('viewcategorydata',views.viewcategorydata,name="viewcategorydata"),
    path('delete_category/<int:id>', views.delete_category, name='delete_category'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    
]

