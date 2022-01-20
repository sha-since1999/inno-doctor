from django.test import TestCase
from patient_records.forms import *
class TestForm(TestCase):
   def test_vital_sign_form_valid_data(self):
        form = VitalSignForm(data={
                'body_weight' :123,
                'height' :123,
                'respiration_rate' :123,
                'pulse_rate' :123,
                'body_temperature' :123,
                'head_circumference' :123,
                'pulse_oximetry' :123,
                'body_mass_index' :123,
                'blood_pressure_systolic' :123,
                'blood_pressure_diastolic' :123,
                
        })
        self.assertTrue(form.is_valid())
    
def test_vital_sign_form_no_data(self):
        form =VitalSignForm(data={})
        self.assertFalse(form.is_valid())
        