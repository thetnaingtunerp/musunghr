from django.urls import path
from .views import *
from . import views
app_name = 'merchant'
urlpatterns = [
    path('test/', views.test, name='test'),
]