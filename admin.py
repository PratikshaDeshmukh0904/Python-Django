from django.contrib import admin

# Register your models here.
from .models import Admin
from .models import branch
from .models import StandardMaster

admin.site.register(Admin)
admin.site.register(branch)
admin.site.register(StandardMaster)