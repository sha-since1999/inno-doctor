from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from patient_records.models import Patient
from patient_records.views import *
class TEST_ALL_URLS(TestCase):
    
    def test_problem_list_create_url_is_resolved(self):
        url = reverse('patient_records:patient_problem_list_create',args=['123'])
        self.assertEqual(resolve(url).func,patientProblemListCreate)
    
    def test_problem_list_view_url_is_resolved(self):
        url = reverse('patient_records:patient_problem_list_view',args=['123'])
        self.assertEqual(resolve(url).func,patientProblemListView)

