# from trash_collector.employees.models import Employee
# from django.http.response import HttpResponseRedirect
# from trash_collector.customers.models import Customer
from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy, reverse
from django.views import generic
from .forms import CustomUserForm


class RegisterView(generic.CreateView):
    """Allows user to register with the custom form we created"""
    form_class = CustomUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration.html'

# def register(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         user = request.POST.get('user')
#         address = request.POST.get('address')
#         zip_code = request.POST.get('zip_code')
#         balance = request.POST.get('balance')
#         weekly_pickup_day = request.POST.get('weekly_pickup_day')
#         one_time_pickup = request.POST.get('one_time_pickup')
#         suspend_start = request.POST.get('suspend_start')
#         suspend_end = request.POST.get('suspend_end')
#         new_customer = Customer(name=name, user=user, address=address, zip_code=zip_code, balance=balance, weekly_pickup_day=weekly_pickup_day, one_time_pickup=one_time_pickup, suspend_start=suspend_start, suspend_end=suspend_end)
#         new_customer.save()
#         return HttpResponseRedirect(reverse('customers:index'))
#     else:
#         return render(request, 'customers/registration.html')

# def employee_register(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         user = request.POST.get('user')
#         zip_code = request.POST.get('zip_code')
#         new_employee = Employee(name=name, user=user, zip_code=zip_code)
#         new_employee.save()
#         return HttpResponseRedirect(reverse('employees:index'))
#     else:
#         return render(request, 'employees/registration.html')

# def home(request):
#     home_page = HttpResponseRedirect(reverse('trash_collector:home'))


# def index(request):
#     all_users = Customer.objects.all()
#     context = {
#         'all_users': all_users
#     }
#     return render(request)