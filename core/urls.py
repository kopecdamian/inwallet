from django.urls import path
from . import views
urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("obligacje/", views.governmentBonds, name="governmentBonds")
]