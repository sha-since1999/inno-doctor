from django.contrib import admin

from .models import (MedicationItem, InternationalPatientSummary,
                     ProblemList,
                     VitalSigns, SocialHistory, MedicationStatement, )

admin.site.register(
	InternationalPatientSummary)

admin.site.register(
		MedicationItem
)
admin.site.register(
		ProblemList
)
admin.site.register(
		VitalSigns
)
admin.site.register(
		SocialHistory
)
admin.site.register(MedicationStatement)
