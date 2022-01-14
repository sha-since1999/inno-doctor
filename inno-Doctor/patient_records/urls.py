from django.urls import path

from .views import (
    EPrescription, PatientView, PatientList,
)

app_name = 'patient_records'

urlpatterns = [
    path('patient_record_form/', PatientView, name='patient_record_form'),
    path('patient_record_list/', PatientList, name='patient_record_list'),
    path('e_prescription/<int:aadhar_id>/', EPrescription,
         name='e_prescription')
]
