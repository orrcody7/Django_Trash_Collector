from customers.models import Customer
from .models import Employee
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.apps import apps
from django.urls import reverse
from django.http.response import HttpResponseRedirect



# Create your views here.


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers
    all_customers = apps.get_model('customers.Customer')
    context = {
        'all_customers': all_customers
    }
    return render(request, 'employees/index.html', context)

def filter(request, weekly_pickup_day):
    filter_day = Customer.objects.filter(weekly_pickup_day=weekly_pickup_day)
    context = {
        'filter_day':filter_day
    }
    return render(request, 'employees/filter.html', context)
    
def route(request):
    change_route = Employee.objects.get(user=request.user)
    if request.method == "POST":
        change_route.zip_code= request.POST.get('zip_code')
        change_route.save()
        return HttpResponse(reverse('employees:index'))
    else:
        context = {
            'change_route': change_route
        }
        return render(request, 'employees/route.html', context)

def account_info(request):
    employees = Employee.objects.get(user=request.user)
    context = {
        'employees': employees
    }
    return render(request, 'employees/account_info.html', context)

def registration(request):
    if request.method == "POST":
        name = request.POST.get('name')
        user = request.user
        zip_code = request.POST.get('zip_code')
        new_employee = Employee(name=name, user=user, zip_code=zip_code)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/registration.html')



