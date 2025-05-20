from django.urls import path
from . import views

app_name = "wallet"
urlpatterns = [
    # Dashboard
    path("", views.dashboard, name="dashboard"),
    # List of government list
    path("bonds/", views.governmentBonds, name="governmentBonds"),
    # Add government bond
    path("bonds/add", views.governmentBondAdd, name="governmentBondAdd"),
]