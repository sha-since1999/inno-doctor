from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from patient_records.models import Patient
from patient_records.views import *
class TEST_ALL_URLS(TestCase):
    

    def test_social_history_create_url_is_resolved(self):
        url = reverse('patient_records:patient_social_histroy_create',args=['123'])
        self.assertEqual(resolve(url).func,patientSocialHistoryCreate)
     
    def test_social_history_update_url_is_resolved(self):
        url = reverse('patient_records:patient_social_histroy_update',args=['123'])
        self.assertEqual(resolve(url).func,patientSocialHistoryUpdate)

    def test_social_history_view_url_is_resolved(self):
        url = reverse('patient_records:patient_social_histroy_view',args=['123'])
        self.assertEqual(resolve(url).func,patientSocialHistoryView)
