from django.contrib import admin

from .models import (DosageInstructions, InternationalPatientSummary,
                     EPrescription,
                     MedicationOrder,
                     ProblemList,
                     VitalSigns, SocialHistory, MedicationStatement, )

admin.site.register(
	InternationalPatientSummary)
admin.site.register(
		EPrescription
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
admin.site.register(
		DosageInstructions
)
admin.site.register(MedicationStatement)
admin.site.register(MedicationOrder)
