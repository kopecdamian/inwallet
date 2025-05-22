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
     # Detail of government bond
    path("bonds/<int:bond_id>", views.governmentBondDetails, name="governmentBondDetails"),
    # Delete of government bond
    path("bonds/<int:bond_id>/delete", views.governmentBondDelete, name="governmentBondDelete"),
]