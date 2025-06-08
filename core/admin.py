from django.contrib import admin

# Register your models here.
from .models import GovernmentBond, BondsTotal, GovernmentBondInterest

admin.site.register(GovernmentBond)
admin.site.register(BondsTotal)
admin.site.register(GovernmentBondInterest)
