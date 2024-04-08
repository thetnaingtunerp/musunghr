from django.urls import path
from .views import *
from . import views
app_name = 'myapp'
urlpatterns = [
    path('test/', views.test, name='test'),
    path('Department_Setup/', Department_Setup.as_view(), name='Department_Setup'),
    path('Position_Setup/', Position_Setup.as_view(), name='Position_Setup'),
    path('Region_Setup/', Region_Setup.as_view(), name='Region_Setup'),
    path('Township_Setup/', Township_Setup.as_view(), name='Township_Setup'),
    path('Employee_List/', Employee_List.as_view(), name='Employee_List'),
    path('EmployeeCreate/', EmployeeCreate.as_view(), name='EmployeeCreate'),

    path('EmpCreate/', EmpCreate.as_view(), name='EmpCreate'),
    path('EmployeeDetailView/<int:pk>/', EmployeeDetailView.as_view(), name='EmployeeDetailView'),
    path('EmployeeAtt/', EmployeeAtt.as_view(), name='EmployeeAtt'),
    path('AttCheckout/', AttCheckout.as_view(), name='AttCheckout'),
    path('DailyAttReport/', DailyAttReport.as_view(), name='DailyAttReport'),

    path('EmployeeGatepass/', EmployeeGatepass.as_view(), name='EmployeeGatepass'),
]
