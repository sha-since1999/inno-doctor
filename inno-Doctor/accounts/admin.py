from django.contrib import admin

from .models import InternationalPatientSummary, EPrescription, ProblemList, \
	VitalSigns, SocialHistory, MedicationStatement

admin.site.register(
	InternationalPatientSummary)
admin.site.register(
		EPrescription
)
admin.site.register( MedicationStatement)
