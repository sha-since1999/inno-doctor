from django.test import TestCase , Client
from django.urls import reverse
from patient_records.models import *
import json

class VitalSignTestViews(TestCase):
    def setUp(self) :
        self.client= Client()
        self.vital_sign_view_url     =  reverse('patient_records:patient_vital_sign_view',args=['123412341234'])
        self.vital_sign_create_url  = reverse('patient_records:patient_vital_sign_create',args=['98475638475'])
        self.vital_sign_edit_url       = reverse('patient_records:patient_vital_sign_edit',args=['123412341234'])
        self.patient1= Patient.objects.create( 
            aadhaarId          = '123412341234',
            name                 = 'unknown',
            date_of_birth    = '2020-01-10',
            gender               = 'Male',
            )
        self.patient2= Patient.objects.create( 
            aadhaarId          = '98475638475',
            name                 = 'unknown2',
            date_of_birth    = '2020-01-10',
            gender               = 'Female',
            )
        self. vital_sign1  = VitalSign.objects.create(
                patient = self.patient1,
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
        vital_sign_view_url=  reverse('patient_records:patient_vital_sign_view',args=['87654356343'])
        response=self.client.get(vital_sign_view_url)
        print(response.status_code)
        self.assertEqual(response.status_code,302)
       
       
        
    def test_vital_sign_create(self):
        response= self.client.post(self.vital_sign_create_url,{
               'body_weight' :123,
                'height' :987,
                'respiration_rate' :123,
                'pulse_rate' :456,
                'body_temperature' :123,
                'head_circumference' :123,
                'pulse_oximetry' :123,
                'body_mass_index' :123,
                'blood_pressure_systolic' :123,
                'blood_pressure_diastolic' :123,
        } )
        
        vital_sign= VitalSign.objects.get(patient=self.patient2)
        self.assertEqual(vital_sign.height,987)
        self.assertEqual(vital_sign.pulse_rate,456)
        
    def test_vital_sign_update(self):
        response= self.client.post(self.vital_sign_edit_url,{
               'body_weight' :123,
                'height' :321,
                'respiration_rate' :123,
                'pulse_rate' : 98.1,
                'body_temperature' :123,
                'head_circumference' :123,
                'pulse_oximetry' :123,
                'body_mass_index' :123,
                'blood_pressure_systolic' :123,
                'blood_pressure_diastolic' :123,
        } )

        vital_sign= VitalSign.objects.get(patient=self.patient1)
        self.assertEqual(vital_sign.height,321)
        self.assertEqual(vital_sign.pulse_rate,98.1)
        