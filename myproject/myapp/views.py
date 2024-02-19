from django.shortcuts import render,redirect
from .models import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from django.db.models import Sum,Count,F
from django.http import HttpResponse
from django.views.generic import TemplateView, View, CreateView, DetailView,FormView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
def test(request):
    return render(request, 'dashboard.html')

class Department_Setup(View):
    def get(self,request):
        dept = department.objects.all()
        context = {'dept':dept}
        return render(request, 'department_setup.html', context)

    def post(self,request):
        dept = department.objects.all()
        dept_name = request.POST.get('department_name')
        message = None
        if not dept_name:
            message = 'please enter department name'
        if not message:
            d = department(department_name=dept_name)
            d.save()
            return redirect(request.META['HTTP_REFERER'])
        else:
            dept = department.objects.all()
            message = 'please enter department name'
            context = {'dept':dept, 'message': message}
            return render(request, 'department_setup.html', context)

class Position_Setup(View):
    def get(self,request):
        pst = position.objects.all()
        context = {'pst':pst}
        return render(request, 'position.html', context)

    def post(self,request):
        pst = position.objects.all()
        pst_name = request.POST.get('position')
        message = None
        if not pst_name:
            message = 'please enter postion name'
        if not message:
            d = position(position=pst_name)
            d.save()
            return redirect(request.META['HTTP_REFERER'])
        else:
            pst = position.objects.all()
            context = {'pst':pst}
            return render(request, 'position.html', context)

class Region_Setup(View):
    def get(self,request):
        st = state_region.objects.all()
        context = {'st':st}
        return render(request, 'region_setup.html', context)

    def post(self,request):
        st = state_region.objects.all()
        st_name = request.POST.get('state_name')
        message = None
        if not st_name:
            message = 'please enter postion name'
        if not message:
            d = state_region(state_name=st_name)
            d.save()
            return redirect(request.META['HTTP_REFERER'])
        else:
            pst = state_region.objects.all()
            context = {'st':st}
            return render(request, 'region_setup.html', context)


