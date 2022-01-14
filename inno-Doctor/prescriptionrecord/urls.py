from django.urls import path

from .views import med_form

app_name = 'prescriptionrecord'

urlpatterns = [
    path('patient_details/prescription', med_form, name='prescription_record'),
    
]