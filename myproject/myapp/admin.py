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


class emp_gatepass_admin(admin.ModelAdmin):
    list_display = ('id', 'employee_name')
admin.site.register(emp_gatepass, emp_gatepass_admin)

class daily_attendance_report_admin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'attendance_day','ot_hour','absent','date')
admin.site.register(daily_attendance_report, daily_attendance_report_admin)


admin.site.register(employee_profile)

admin.site.register(education_profile)
admin.site.register(work_exp)
admin.site.register(gender)
admin.site.register(marital)
admin.site.register(type)
admin.site.register(edu_grade)
admin.site.register(employee_attendance)