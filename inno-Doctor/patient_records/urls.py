from django.urls import path
from . import views
from .models import Patient
app_name = 'patient_records'

urlpatterns = [
    
     path('patient-check', views.patientCheck, name='patient_check'),
    path('patient-details/',views.patientDetails, name ='patient_details'),
    path('patient-detail/<int:id>',views.patientDetail, name ='patient_detail'),
    path('patient-create/', views.patientCreate, name='patient_create'),
    path('patient-problem-list/<int:id>', views.patientProblemList, name='patient_problem_list'),
    path('patient-medication-statement/<int:id>', views.medicationStatementCreate, name='add_new_patient_medication_statement_by_POST'),
    path('patient-update/<int:id>', views.patientUpdate, name='patient_update'),
    path('patient-eprescription/<int:id>', views.eprescriptionList, name='eprescription'),

    path('patient_record_form/', views.PatientView, name='patient_record_form'),
    path('patient_record_list/', views.PatientList, name='patient_record_list'),
]