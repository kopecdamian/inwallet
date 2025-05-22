from django.contrib import admin

# Register your models here.
from .models import GovernmentBond, BondsTotal

admin.site.register(GovernmentBond)
admin.site.register(BondsTotal)
