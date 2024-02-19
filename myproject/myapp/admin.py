from django.contrib import admin
from .models import *
# Register your models here.

class departmentadmin(admin.ModelAdmin):
    list_display = ('id','department_name','created_at','updated_at')
admin.site.register(department,departmentadmin)

class positionadmin(admin.ModelAdmin):
    list_display = ('id','position','created_at','updated_at')
admin.site.register(position,positionadmin)


class stateadmin(admin.ModelAdmin):
    list_display = ('id','state_name','created_at','updated_at')
admin.site.register(state_region,stateadmin)

class townshipadmin(admin.ModelAdmin):
    list_display = ('id','township','state','created_at','updated_at')
admin.site.register(township,townshipadmin)
