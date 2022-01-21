from django.test import SimpleTestCase
from django.urls import reverse, resolve
from patient_records.views import PatientView, PatientList

class TestUrls(SimpleTestCase):
    def test_patient_form_url_is_resolved(self):
        url = reverse('patient_records:patient_record_form')
        self.assertEquals(resolve(url).func, PatientView)

    def test_patient_list_url_is_resolved(self):
        url = reverse('patient_records:patient_record_list')
        self.assertEquals(resolve(url).func, PatientList)