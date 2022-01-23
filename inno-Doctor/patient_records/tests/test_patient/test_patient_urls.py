from django.test import SimpleTestCase
from django.urls import reverse, resolve
from patient_records.views import *

class TestUrls(SimpleTestCase):
    def test_patient_create_url_is_resolved(self):
        url = reverse('patient_records:patient_create' )
        print(resolve(url))
        self.assertEqual(resolve(url).func, patientCreate)

    def test_patient_details_POST_url_is_resolved(self):
        url = reverse('patient_records:patient_details')
        self.assertEqual(resolve(url).func, patientDetails)
        
    def test_patient_check_url_is_resolved(self):
        url = reverse('patient_records:patient_check')
        self.assertEqual(resolve(url).func, patientCheck)
        
    def test_patient_detail_GET_url_is_resolved(self):
        url = reverse('patient_records:patient_detail',args=['123412341234'])
        self.assertEqual(resolve(url).func, patientDetail)
        
    def test_patien_update_url_is_resolved(self):
        url = reverse('patient_records:patient_update' ,args=['123412341234'])
        self.assertEqual(resolve(url).func, patientUpdate)
        