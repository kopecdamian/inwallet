from django.db import models

# Table: Government Bond
class GovernmentBond(models.Model):
    BOND_TYPES = [
        ('EDO', 'EDO – 10 letnie'),
        ('COI', 'COI – 4 letnie'),
        ('TOS', 'TOS – 3 letnie'),
    ]

    INTEREST_TYPES = [
        ('fixed', 'Stałe'),
        ('variable', 'Zmienne'),
        ('inflation', 'indeksowane inflacją'),
    ]

    name = models.CharField(max_length=20)
    bond_type = models.CharField(max_length=4, choices=BOND_TYPES)
    interest_type = models.CharField(max_length=10, choices=INTEREST_TYPES)
    purchase_date = models.DateField()
    maturity_date = models.DateField()
    face_value = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    return_rate = models.DecimalField(max_digits=10,  decimal_places=4)
    profit = models.DecimalField(max_digits=10, decimal_places=2)
    is_redeemed = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class BondsTotal(models.Model):
    BOND_TYPES = [
        ('EDO', 'EDO – 10 letnie'),
        ('COI', 'COI – 4 letnie'),
        ('TOS', 'TOS – 3 letnie'),
    ]
    bond_type = models.CharField(max_length=4, choices=BOND_TYPES)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    updated_at = models.DateTimeField(auto_now_add=True) 
    def __str__(self):
        return f"{self.bond_type}: {self.total} zł"
    
class GovernmentBondInterest(models.Model):
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    year_order = models.DecimalField(max_digits=2, decimal_places=0)
    government_bond = models.ForeignKey(GovernmentBond, on_delete=models.CASCADE)
    def __str__(self):
        return self.interest_rate