from django.db import models

# Table: Government Bond
class GovernmentBond(models.Model):
    BOND_TYPES = [
        ('EDO', 'EDO – 10-year'),
        ('COI', 'COI – 4-year'),
        ('ROS', 'ROS – 3-year'),
        ('ROR', 'ROR – 2-year'),
    ]

    INTEREST_TYPES = [
        ('fixed', 'Fixed'),
        ('variable', 'Variable'),
        ('inflation', 'Inflation-indexed'),
    ]

    name = models.CharField(max_length=20)
    bond_type = models.CharField(max_length=4, choices=BOND_TYPES)
    purchase_date = models.DateField()
    maturity_date = models.DateField()
    face_value = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    interest_type = models.CharField(max_length=10, choices=INTEREST_TYPES)
    return_rate = models.DecimalField(max_digits=10,  decimal_places=4)
    profit = models.DecimalField(max_digits=10, decimal_places=2)
    is_redeemed = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class BondsTotal(models.Model):
    BOND_TYPES = [
        ('EDO', 'EDO – 10-year'),
        ('COI', 'COI – 4-year'),
        ('ROS', 'ROS – 3-year'),
        ('ROR', 'ROR – 2-year'),
    ]
    bond_type = models.CharField(max_length=4, choices=BOND_TYPES)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    updated_at = models.DateTimeField(auto_now_add=True) 
    def __str__(self):
        return f"{self.bond_type}: {self.total} zł"