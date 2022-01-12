from django.contrib import admin

# Register your models here.
from .models import InternationalPatientSummary, EPrescription, ProblemList, \
	VitalSigns, SocialHistory, MedicationStatement

admin.site.register(InternationalPatientSummary)
admin.site.register(EPrescription)
admin.site.register( MedicationStatement)
admin.site.register( ProblemList)
admin.site.register( VitalSigns)
admin.site.register( SocialHistory)
