from django.urls import path
from . import views
from .models import Patient
app_name = 'patient_records'

urlpatterns = [
    
    path('patient-check', views.patientCheck, name='patient_check'),
    path('patient-details/',views.patientDetails, name ='patient_details'),
    path('patient-detail/<int:id>',views.patientDetail, name ='patient_detail'),
    path('patient-create/<int:id>', views.patientCreate, name='patient_create'),

    path('patient-create/', views.patientCreate, name='patient_create'),


    path('patient-problem-list-create/<int:id>', views.patientProblemListCreate, name='patient_problem_list_create'),
    path('patient-social-history-create/<int:id>', views.patientSocialHistoryCreate, name='patient_social_histroy_create'),
    path('patient-social-history-edit/<int:id>', views.patientSocialHistoryUpdate, name='patient_social_histroy_update'),
    path('patient-vital-sign-create/<int:id>', views.patientVitalSignCreate, name='patient_vital_sign_create'),
   
    path('patient-problem-list-view/<int:id>', views.patientProblemListView, name='patient_problem_list_view'),
    path('patient-social-history-view/<int:id>', views.patientSocialHistoryView, name='patient_social_histroy_view'),
    path('patient-vital-sign-view/<int:id>', views.patientVitalSignView, name='patient_vital_sign_view'),
    path('patient-vital-sign-edit/<int:id>', views.patientVitalSignUpdate, name='patient_vital_sign_edit'),
   
    path('patient-medication-statement/<int:id>', views.medicationStatementCreate, name='add_new_patient_medication_statement_by_POST'),
    path('patient-update/<int:id>', views.patientUpdate, name='patient_update'),
    path('patient-eprescription/<int:id>', views.eprescriptionList, name='eprescription'),
    path('patient-eprescription-create/<int:id>', views.eprescriptionCreate, name='eprescription-create'),

    path('patient_record_form/', views.PatientView, name='patient_record_form'),
    path('patient_record_list/', views.PatientList, name='patient_record_list'),
    
]




