from django.urls import path
from . import views
from .models import Patient
app_name = 'patient_records'

urlpatterns = [
    
     path('patient-check', views.patientCheck, name='patient-check'),
    path('patient-details/',views.patientDetails, name ='patient-details'),
    path('patient-detail/<int:id>',views.patientDetail, name ='patient-detail'),
    path('patient-create/', views.patientCreate, name='patient-create'),
    path('patient-problem-list/<int:id>', views.patientProblemList, name='patient-problem-list'),
    path('patient-update/<int:id>', views.patientUpdate, name='patient-update'),
    path('patient-eprescription/<int:id>', views.eprescriptionList, name='eprescription'),

    path('patient_record_form/', views.PatientView, name='patient_record_form'),
    path('patient_record_list/', views.PatientList, name='patient_record_list'),
]