from django import forms
from django.forms import inlineformset_factory
from .models import GovernmentBond, GovernmentBondInterest

class GovernmentBondForm(forms.ModelForm):
    class Meta:
        model = GovernmentBond
        fields = ['name', 'bond_type', 'purchase_date', 'face_value', 'quantity', 'interest_type', 'is_redeemed', 'notes']
        labels = {
            "name":  "Nazwa *",
            "bond_type": "Rodzja ogligacji *",
            "purchase_date": "Data zakupu *",
            "face_value": "Wartość początkowa *",
            "quantity": "Ilość *",
            "interest_rate": "Oprocentowanie *",
            "interest_type": "Rodzaj oprocentowania *",
            "is_redeemed": "Wykupione? *",
            "notes": "Komentarz",
            
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'Podaj nazwę'}),
            'bond_type': forms.Select(attrs={'class': 'form-control'}),
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
            'face_value': forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'Podaj nazwę klienta'}),
            'quantity': forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'Podaj nazwę klienta'}),
            'interest_rate': forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'Podaj nazwę klienta'}),
            'interest_type': forms.Select(attrs={'class': 'form-control'}),
            'is_redeemed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'notes': forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'Komentarz'}),
        }

InterestFormSet = inlineformset_factory(
    GovernmentBond, GovernmentBondInterest,
    fields=['interest_rate', 'year_order'],
    extra=1, can_delete=True
)