from django.shortcuts import get_object_or_404, render
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

    return render(request, "governmentBondForm.html", {"form": form})

# Detail of government bond
def governmentBondDetails(request, bond_id):
    bond = get_object_or_404(GovernmentBond, pk=bond_id)
    if request.method == "POST":
        form = GovernmentBondForm(request.POST, instance=bond)
        if form.is_valid():
            bond = form.save()
            return HttpResponseRedirect(reverse("wallet:governmentBonds"))
    else:
        form = GovernmentBondForm(instance=bond)

    return render(request, "governmentBondForm.html", {"form": form})

# Delete of government bond
def governmentBondDelete(request, bond_id):
    bond = get_object_or_404(GovernmentBond, pk=bond_id)
    if request.method == "POST":
        bond.delete()
        return HttpResponseRedirect(reverse("wallet:governmentBonds"))
    return HttpResponseRedirect(reverse("wallet:governmentBonds"))