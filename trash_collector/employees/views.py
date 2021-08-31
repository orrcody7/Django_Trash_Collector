from trash_collector.employees.models import Employee
from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps
from django.urls import reverse
from django.http.response import HttpResponseRedirect

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers
    Customer = apps.get_model('customers.Customer')
    # filter customers by zip code, weekly pickup day, suspended
    return render(request, 'employees/index.html')

def route(request):
    change_route = Employee.objects.get(user=request.user)
    if request.method == "POST":
        change_route.zip_code= request.POST.get('zip_code')
        change_route.save()
        return HttpResponseRedirect(reverse('employees:index'))
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
