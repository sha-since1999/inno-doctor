from django.test import SimpleTestCase
from django.urls import reverse, resolve
from patient_records.views import *

class TestUrls(SimpleTestCase):
    def test_add_vital_sign_form_url_is_resolved(self):
        url = reverse('patient_records:patient_vital_sign_create' ,args=['123412341234'])
        print(resolve(url))
        self.assertEqual(resolve(url).func, patientVitalSignCreate)

    def test_check_vital_sign_url_is_resolved(self):
        url = reverse('patient_records:patient_vital_sign_view',args=['123412341234'])
        self.assertEqual(resolve(url).func, patientVitalSignView)
        
    def test_edit_vital_sign_url_is_resolved(self):
        url = reverse('patient_records:patient_vital_sign_edit',args=['123412341234'])
        self.assertEqual(resolve(url).func, patientVitalSignUpdate)
        