from django.test import TestCase
from patient_records.forms import *

class TestModel(TestCase):

    def test_patient_form_valid_data(self):
        form = PatientForm(data={
            'aadhaarId'          :'12341234122',
            'name'                 : 'geeta',
            'date_of_birth'    :'2020-01-10',
            'gender'               : 'M',
        })
        self.assertTrue(form.is_valid())
    
    def test_patient_form_no_data(self):
        form = PatientForm(data={})
        self.assertFalse(form.is_valid())
        