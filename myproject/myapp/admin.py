from django.contrib import admin
from .models import *
# Register your models here.

class departmentadmin(admin.ModelAdmin):
    list_display = ('id','department_name','created_at','updated_at')
admin.site.register(department,departmentadmin)




