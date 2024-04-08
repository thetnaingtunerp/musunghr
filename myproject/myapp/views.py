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


from django.forms import modelformset_factory
from django.urls import reverse

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

class Township_Setup(View):
    def get(self, request):
        ts = township.objects.all()
        st = state_region.objects.all()
        context = {'ts':ts, 'st':st}
        return render(request, 'township_setup.html', context)
    
    def post(self,request):
        st_name = request.POST.get('state')
        ts_name = request.POST.get('township')
        message = None
        if not st_name:
            message = 'please enter state name'
        if not message:
            d = township(state=st_name,township=ts_name)
            d.save()
            return redirect(request.META['HTTP_REFERER'])
        else:
            ts = township.objects.all()
            st = state_region.objects.all()
            context = {'ts':ts, 'st':st, 'message':message}
            return render(request, 'township_setup.html', context)

class Employee_List(View):
    def get(self, request):
        emp = employee_profile.objects.all()
        context = {'emp':emp}
        return render(request, 'employee_list.html', context)

class EmployeeCreate(CreateView):
    template_name = 'employee_create.html'
    form_class = employee_profile_form
    success_url = reverse_lazy('myapp:Employee_List')


class EmployeeDetailView(DetailView):
    # specify the model to use
    model = employee_profile
    template_name = 'employee_detail.html'
 
    # override context data
    def get_context_data(self, *args, **kwargs):
        context = super(EmployeeDetailView,
             self).get_context_data(*args, **kwargs)
        # add extra field 
        context["msg"] = "MISC"        
        return context






class EmpProfileInline():
    form_class = employee_profile_form
    model = employee_profile
    template_name = "employee_create.html"

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save()

        # for every formset, attempt to find a specific formset save function
        # otherwise, just save.
        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.save()
        return redirect('myapp:Employee_List')

    def formset_variants_valid(self, formset):
        """
        Hook for custom formset saving.. useful if you have multiple formsets
        """
        variants = formset.save(commit=False)  # self.save_formset(formset, contact)
        # add this, if you have can_delete=True parameter set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for variant in variants:
            variant.employee_name = self.object
            variant.save()

    def formset_images_valid(self, formset):
        """
        Hook for custom formset saving.. useful if you have multiple formsets
        """
        images = formset.save(commit=False)  # self.save_formset(formset, contact)
        # add this, if you have can_delete=True parameter set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for image in images:
            image.employee_name = self.object
            image.save()


class EmpCreate(EmpProfileInline, CreateView):

    def get_context_data(self, **kwargs):
        ctx = super(EmpCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                'variants': EduFormSet(prefix='variants'),
                'images': WorkexpFormSet(prefix='images'),
            }
        else:
            return {
                'variants': EduFormSet(self.request.POST or None, self.request.FILES or None, prefix='variants'),
                'images': WorkexpFormSet(self.request.POST or None, self.request.FILES or None, prefix='images'),
            }


# Employee Attendance
class EmployeeAtt(View):
    def get(self,request):
        d = datetime.datetime.now()
        emp = employee_attendance.objects.filter(created_at=d).order_by('-id')
        message = None
        context = {'emp':emp, 'message':message}
        return render(request, 'employee_att.html', context)
    
    def post(self, request):
        e = request.POST.get('emp')
        d=datetime.datetime.now()
        
        message = None
        if not e:
            message = "Please Scan Again"
            emp = employee_attendance.objects.filter(created_at=d).order_by('-id')
            context = {'emp':emp, 'message':message}
            return render(request, 'employee_att.html', context)

        else:
                try:
                    emp_obj = employee_profile.objects.get(id=e)
                    e_save = employee_attendance(employee=emp_obj, entry_time=d)
                    e_save.save()
           
                    emp = employee_attendance.objects.filter(created_at=d).order_by('-id')
                    
                    success = "Success"
                    context = {'emp':emp, 'success':success, 'emp_obj':emp_obj}
                    return render(request, 'employee_att.html', context)
                except employee_profile.DoesNotExist:
                    emp = employee_attendance.objects.filter(created_at=d).order_by('-id')
                    message = "Attendance Fail Try Again"
                    context = {'emp':emp, 'message':message}
                    return render(request, 'employee_att.html', context)

        
class AttCheckout(View):
    def get(self, request):
        d = datetime.datetime.now()
        emp = employee_attendance.objects.filter(created_at=d).order_by('-id')
        message = None
        context = {'emp':emp, 'message':message}
        return render(request, 'AttCheckout.html', context)

    def post(self, request):
        e = request.POST.get('emp')
        d=datetime.datetime.now()
        
        message = None
        if not e:
            message = "Please Scan Again"
            emp = employee_attendance.objects.filter(created_at=d).order_by('-id')
            context = {'emp':emp, 'message':message}
            return render(request, 'AttCheckout.html', context)

        else:
                try:
                    emp_obj = employee_profile.objects.get(id=e)
                    emp_check = employee_attendance.objects.filter(created_at=d, employee=emp_obj)
                    if emp_check:
                        emp_check = employee_attendance.objects.filter(created_at=d, employee=emp_obj).update(checkout_time=d)
                    else:
                        emp = employee_attendance.objects.filter(created_at=d).order_by('-id')
                        message = "Checkout Fail Try Again"
                        context = {'emp':emp, 'message':message}
                        return render(request, 'AttCheckout.html', context)
                    # emp_check = employee_attendance.objects.filter(created_at=d, employee=emp_obj).update(checkout_time=d)
                    # e_save = employee_attendance(employee=emp_obj, entry_time=d)
                    # e_save.save()
           
                    emp = employee_attendance.objects.filter(created_at=d).order_by('-id')
                    
                    success = "Success"
                    context = {'emp':emp, 'success':success, 'emp_obj':emp_obj}
                    return render(request, 'AttCheckout.html', context)
                except employee_profile.DoesNotExist:
                    emp = employee_attendance.objects.filter(created_at=d).order_by('-id')
                    message = "Attendance Fail Try Again"
                    context = {'emp':emp, 'message':message}
                    return render(request, 'AttCheckout.html', context)                

class DailyAttReport(View):
    def get(self, request):
        d=datetime.datetime.now()
        emp = employee_attendance.objects.filter(created_at=d)
        success = "Success"
        context = {'emp':emp, 'success':success}
        return render(request, 'DailyAttReport.html', context)

    def post(self, request):
        pass

            
        
# Start Gate Pass Section
class EmployeeGatepass(View):
    def get(self, request):
        gp = emp_gatepass.objects.all()
        emp = employee_profile.objects.all()
        context = {'gp':gp, 'emp':emp}
        return render(request, 'EmployeeGatepass.html', context)

# End Gate Pass Section

