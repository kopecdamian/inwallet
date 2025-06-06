from django.shortcuts import get_object_or_404, render
from .models import GovernmentBond, BondsTotal
from .forms import GovernmentBondForm
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

def sum_bonds_by_type(bond_type):
    all_bonds_by_type = GovernmentBond.objects.filter(bond_type = bond_type)
    total = 0
    for bond in all_bonds_by_type:
        total += bond.face_value
    if BondsTotal.objects.filter(bond_type=bond_type).exists():
        BondsTotal.objects.filter(bond_type=bond_type).update(total=total)
    else:
        BondsTotal.objects.create(bond_type=bond_type, total = total)

def calculate_government_bond_profit(bond_data):
    purchase_date = bond_data.purchase_date
    if bond_data.bond_type == 'EDO':
        maturity_date = purchase_date + relativedelta(years=10)
    elif bond_data.bond_type == 'COI':
        maturity_date = purchase_date + relativedelta(years=4)
    elif bond_data.bond_type == 'ROS':
        maturity_date = purchase_date + relativedelta(years=3)
    elif bond_data.bond_type == 'ROR':
        maturity_date = purchase_date + relativedelta(years=2)
    bond_data.maturity_date = maturity_date
        
    today = date.today()
    days_number = (today - purchase_date).days
    profit = bond_data.face_value * bond_data.interest_rate/100/365*days_number
    bond_data.profit = profit

    bond_data.return_rate = profit / bond_data.face_value * 100
    bond_data.save()    

# Dashboard
def dashboard(request):
    bond_totals = BondsTotal.objects.filter(total__gt = 0)

    context = {
        "bond_totals": bond_totals
    }
    return render(request, "dashboard.html", context)

# List of government bonds
def governmentBonds(request):
    all_bonds = GovernmentBond.objects.filter()
    context = {
        "all_bonds": all_bonds,
    }
    return render(request, "governmentBonds.html", context)

# Add government bond
def governmentBondAdd(request):
    if request.method == "POST":
        form = GovernmentBondForm(request.POST)
        if form.is_valid():
            new_bond = form.save(commit=False)
            calculate_government_bond_profit(new_bond)
            sum_bonds_by_type(new_bond.bond_type)
            return HttpResponseRedirect(reverse("wallet:governmentBonds"))
    else:
        form = GovernmentBondForm()

    return render(request, "governmentBondForm.html", {"form": form})

# Detail of government bond
def governmentBondDetails(request, bond_id):
    bond = get_object_or_404(GovernmentBond, pk=bond_id)
    old_bond_type = bond.bond_type
    if request.method == "POST":
        form = GovernmentBondForm(request.POST, instance=bond)
        if form.is_valid():
            updated_bond = form.save(commit=False)
            calculate_government_bond_profit(updated_bond)
            sum_bonds_by_type(old_bond_type)
            sum_bonds_by_type(updated_bond.bond_type)
            return HttpResponseRedirect(reverse("wallet:governmentBonds"))
    else:
        form = GovernmentBondForm(instance=bond)

    return render(request, "governmentBondForm.html", {"form": form})

# Delete of government bond
def governmentBondDelete(request, bond_id):
    bond = get_object_or_404(GovernmentBond, pk=bond_id)
    bond_type = bond.bond_type
    if request.method == "POST":
        bond.delete()
        sum_bonds_by_type(bond_type)
        return HttpResponseRedirect(reverse("wallet:governmentBonds"))
    return HttpResponseRedirect(reverse("wallet:governmentBonds"))