from django.urls import path

from .views import (
    PatientView, PatientList, ProblemAddPage, SocialHistoryPage, VitalSignPage,
)

app_name = 'patient_records'

urlpatterns = [
    path('patient_record_form/', PatientView, name='patient_record_form'),
    path('patient_record_list/', PatientList, name='patient_record_list'),
    path('vital_signs/', VitalSignPage, name='vital_signs'),
    path('social_history/', SocialHistoryPage, name = 'social_history'),
    path('problem_list/', ProblemAddPage, name= "problem_list")
]
