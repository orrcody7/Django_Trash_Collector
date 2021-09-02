from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('filter/<str:weekly_pickup_day>', views.filter, name="filter"),
    path('route/', views.route, name="route"),
    path('account_info/', views.account_info, name="account_info"),
    path('registration/', views.registration, name="registration")
]