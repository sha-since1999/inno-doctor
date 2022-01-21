from django.test import TestCase
from patient_records.models import *

class TestModel(TestCase):
    def setUp(self):
        self.patient1= Patient.objects.create( 
            aadhaarId          = 123412341234,
            name                 = 'unknown',
            date_of_birth    = '2020-01-10',
            gender               = 'Male',
            )
        self.vital_sign= VitalSign.objects.create( 
                                                  
                patient=self.patient1,
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
        
    def test_model_vital_sign_methods(self):
        vital_sign= VitalSign.objects.get(patient=self.patient1)
        self.assertEqual(vital_sign.height,123)
        
        #we have no method in vital_sign model to test