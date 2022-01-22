from django.contrib import admin
from django.db.models.base import Model
from .models import Patient

# Register your models here

admin.site.register(Patient)