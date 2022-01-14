from django.contrib import admin

from .models import (MedicationItem, Patient,
                     ProblemList,
                     VitalSign, SocialHistory, MedicationStatement, )
admin.site.register(
	Patient)

admin.site.register(
		MedicationItem
)
admin.site.register(
		ProblemList
)
admin.site.register(
		VitalSign
)
admin.site.register(
		SocialHistory
)
admin.site.register(MedicationStatement)