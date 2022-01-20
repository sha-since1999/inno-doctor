from django.test import TestCase , Client
from django.urls import reverse
from patient_records.models import *
import json

class VitalSignTestViews(TestCase):
    def setUp(self) :
        self.client= Client()
        self.vital_sign_view_url     =   reverse('patient_records:patient_vital_sign_view',args=['123412341234'])
        self.vital_sign_create_url  =  reverse('patient_records:patient_vital_sign_create',args=['123412341234'])
        self.vital_sign_edit_url      =  reverse('patient_records:patient_vital_sign_edit',args=['123412341234'])
        self. vital_sign_test_obj    =  VitalSign.objects.create(
                id=1,
                patient = 123412341234,
                body_weight = 123,
                height = 123,
                respiration_rate = 123,
                pulse_rate = 123,
                body_temperature = 123,
                head_circumference = 123,
                pulse_oximetry = 123,
                body_mass_index = 123,
                blood_pressure_systolic = 123,
                blood_pressure_diastolic = 123,
        )
        
    def test_vital_sign_view_should_pass(self):
        vital_sign_view_url=  reverse('patient_records:patient_vital_sign_view',args=['123412341234'])
        response=self.client.get(vital_sign_view_url)
        print(response.status_code)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'patient_records/patient-vital-sign-view.html')
        
    def test_vital_sign_view_when_no_data(self):
        vital_sign_view_url=  reverse('patient_records:patient_vital_sign_view',args=['2542345365'])
        response=self.client.get(vital_sign_view_url)
        print(response.status_code)
        self.assertEqual(response.status_code,404)
        self.assertTemplateUsed(response,'patient_records/patient-detail.html')
        
    # def test_vital_sign_create(self):
    #     pass
    # def test_vital_sign_update(self):
    #     pass

        