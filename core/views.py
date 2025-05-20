from django.shortcuts import render
from .models import GovernmentBond
from .forms import GovernmentBondForm
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
 
# Create your views here.
from django.http import HttpResponse

# Dashboard
def dashboard(request):
    return HttpResponse("Dashboard")

# List of government bonds
def governmentBonds(request):
    all_bonds = GovernmentBond.objects.filter()
    context = {
        "all_bonds": all_bonds,
    }
    return render(request, "bonds.html", context)

# Add government bond
def governmentBondAdd(request):
    if request.method == "POST":
        form = GovernmentBondForm(request.POST)
        if form.is_valid():
            bond = form.save()
            return HttpResponseRedirect(reverse("wallet:governmentBonds"))
    else:
        form = GovernmentBondForm()

    return render(request, "GovernmentBondForm.html", {"form": form})