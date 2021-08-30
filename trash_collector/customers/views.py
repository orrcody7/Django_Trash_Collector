from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Customer
from django.urls import reverse
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in user (if there is one) within any view function
    user = request.user

    try:
        # This line inside the 'try' will return the customer record of the logged-in user if one exists
        logged_in_customer = Customer.objects.get(user=user)
    except:
        # TODO: Redirect the user to a 'create' function to finish the registration process if no customer record found
        return HttpResponseRedirect(reverse('customers:create'))

    # It will be necessary while creating a Customer/Employee to assign request.user as the user foreign key

    print(user)
    return render(request, 'customers/index.html')

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        user = request.user
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        weekly_pickup_day = request.POST.get('weekly_pickup_day')
        new_customer = Customer(name=name, user=user, address=address, zip_code=zip_code, weekly_pickup_day=weekly_pickup_day)
        new_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/create.html')

def edit(request):
    edited_customer = Customer.objects.get()
    if request.method == "POST":
        user = request.user
        edited_customer.address = request.POST.get('address')
        edited_customer.zip_code = request.POST.get('zip_code')
        edited_customer.weekly_pickup_day = request.POST.get('weekly_pickup_day')
        edited_customer.one_time_pickup = request.POST.get('one_time_pickup')
        edited_customer.suspend_start = request.POST.get('suspend_start')
        edited_customer.suspend_end = request.POST.get('suspend_end')
        edited_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        context = {
            'edited_customer': edited_customer
        }
        return render(request, 'customers/edit.html', context)

def display_account(request):
    user = request.user
    customers = Customer.objects.get()
    context = {
        'customers': customers
    }
    return render(request, 'customers/display_account.html', context)

def suspend(request):
    suspend_dates = Customer.objects.get()
    if request.method == "POST":
        user = request.user
        suspend_dates.suspend_start = request.POST.get('suspend_start')
        suspend_dates.suspend_end = request.POST.get('suspend_end')
        suspend_dates.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        context = {
            'suspend_dates':suspend_dates
        }
        return render(request, 'customers/suspend.html', context)
