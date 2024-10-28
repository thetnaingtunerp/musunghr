from django.shortcuts import render,redirect,get_object_or_404, HttpResponse
from .models import *
from .form import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from django.db.models import Sum,Count,F
from django.http import HttpResponse
from django.views.generic import TemplateView, View, CreateView, DetailView,FormView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import datetime

# Create your views here.
def test(request):
    return HttpResponse('helo test 123')