from django.forms import models
from django.test import TestCase
from django.urls import path, reverse
from . import views

# from .models import Patient

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from patient_records.views import patientCreate,patientCheck

app_name = 'patient_records'

from .models import (Patient)
# class PatientModelTest(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         # Set up non-modified objects used by all test methods
#         patientCreate.objects.create(first_name='Batman')

#     def test_aadhaarId(self):
#         author = patientCreate.objects.get(id=1)
#         field_label = author._meta.get_field('aadhaarId').verbose_name
#         self.assertEqual(field_label, 'aadhaarId')



#     def test_first_name_label(self):
#         author = patientCreate.objects.get(id=1)
#         field_label = author._meta.get_field('first_name').verbose_name
#         self.assertEqual(field_label, 'first name')


#     def test_first_name_max_length(self):
#         author = patientCreate.objects.get(id=1)
#         max_length = author._meta.get_field('first_name').max_length
#         self.assertEqual(max_length, 100)



#     def test_date_of_birth(self):
#         author = patientCreate.objects.get(id=1)
#         field_label = author._meta.get_field('date_of_birth').verbose_name
#         self.assertEqual(field_label, 'date_of_birth')


#     def test_get_absolute_url(self):
#         author = patientCreate.objects.get(id=1)
#         # This will also fail if the urlconf is not defined.
#         self.assertEqual(author.get_absolute_url(), '/patient_records/patientCreate/1')



# class TEST_ALL_URLS(SimpleTestCase):
#     def test_change_profile_url_is_resolved(self):
#         url = reverse('patient_records: patientCreate')
#         self.assertEqual(resolve(url).func.view_class,patientCreate)







# test_models.py
class StudentModelTestcase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Patient.objects.create(aadhaarId ="123412341234",name="John")

    def test_string_method(self):
        patient= Patient.objects.get(id=1)
        expected_string = f"Name:{patient.name} {patient.aadhaarId}"
        self.assertEqual(str(patient), expected_string)

    def test_get_absolute_url(self):
        student = Patient.objects.get(id=1)
        self.assertEqual(student.get_absolute_url(), "/patients/1")