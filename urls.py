from django.urls import path

from .import views
from .models import branch
from .models import StandardMaster


urlpatterns = [
path('',views.home,name='home'),
path('registration', views.registration, name="registration"),
path('adminlogin',views.adminlogin,name="adminlogin"),
path('studentlogin',views.studentlogin,name="studentlogin"),
path('stafflogin',views.stafflogin,name="stafflogin"),
path('dologin',views.dologin,name="dologin"),
path('admindashboard',views.admindashboard,name="admindashboard"),
path('branchmaster',views.branchmaster,name="branchmaster"),
path('viewbranchdata',views.viewbranchdata,name="viewbranchdata"),
path('standard',views.standard,name='standard'),
path('staffregister',views.staffregister,name='staffregister'),
# path('admindashboard',views.admindashboard,name="admindashboard"),

]