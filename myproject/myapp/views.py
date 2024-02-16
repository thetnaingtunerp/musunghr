from django.shortcuts import render
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
        pass

# class CategoryCreate(View):
#     def get(self,request):
#         category = Category.objects.all()
#         item_list = Items.objects.all()
#         message = None
#         context = {'item_list': item_list, 'category': category, 'message': message}
#         return render(request, 'categorycreate.html', context)
#     def post(self,request):
#         category_name = request.POST.get('category_name')
#         message = None
#         if not category_name:
#             message = 'please enter category name'
#         if not message:
#             cate = Category(category_name=category_name)
#             cate.save()
#             return redirect(request.META['HTTP_REFERER'])
#         else:
#             category = Category.objects.all()
#             message = 'please enter category name'
#             return render(request, 'categorycreate.html', {'message':message,'category':category})

