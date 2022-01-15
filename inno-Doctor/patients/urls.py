from django.urls import path
from . import views 
from django.conf.urls import url
from .views import PatientViewSet
app_name = 'patients'

urlpatterns = [
    
    path('patient-check', views.patientCheck, name='patient-check'),
    path('patient-details/',views.patientDetails, name ='patient-details'),
    path('patient-create/', views.patientCreate, name='patient-create'),
    path('patient-update/<int:id>', views.patientUpdate, name='patient-update'),

     url(r'^patient/$', PatientViewSet.as_view(
        {
            'get': 'retrieve',
            'post': 'create',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }
    ) ),
    url(r'^patient/all$', PatientViewSet.as_view(
        {
            'get': 'list',
        }
    )),
    ]
