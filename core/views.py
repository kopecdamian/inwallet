from django.shortcuts import render
from .models import GovernmentBond

# Create your views here.
from django.http import HttpResponse

def dashboard(request):
    return HttpResponse("Dashboard")

def governmentBonds(request):
    all_bonds = GovernmentBond.objects.filter()
    context = {
        "all_bonds": all_bonds,
    }
    return render(request, "bonds.html", context)