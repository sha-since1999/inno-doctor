from django.test import TestCase
from patient_records.models import Patient

class TestModel(TestCase):
    def setUp(self):
        self.patient1= Patient.objects.create( 
            aadhaarId          = 123412341234,
            name                 = 'unknown',
            date_of_birth    = '2020-01-10',
            gender               = 'Male',
            )
        
    def test_model_patient_methods(self):
        pass;
        #we have no method in patient model to test