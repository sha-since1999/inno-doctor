from django.urls import path
from .views import VitalSignPage
from django.conf.urls import url
app_name = 'vitalsign'

urlpatterns = [
    
    path('vital-sign', VitalSignPage, name='vital-signs'),
    ]
