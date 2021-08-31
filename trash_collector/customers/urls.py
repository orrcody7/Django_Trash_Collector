from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('edit/', views.edit, name="edit"),
    path('suspend/', views.suspend, name="suspend"),
    path('display_account/', views.display_account, name="display_account"),
    path('request/', views.customer_request, name="customer_request")
]
