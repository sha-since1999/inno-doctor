# from django.urls import path, reverse
# from patient_records.models import Patient
# from django.test import SimpleTestCase
# # from unittest import TestCase
# from django.urls import resolve
# from patient_records.views import patientCreate,patientCheck, patientDetail,patientDetails,PatientList,PatientView
# app_name = 'patient_records'

# class TestUrls(SimpleTestCase):

#     def test_for_patientcheck_resolves(self):
#         url = reverse('patient_records:patient_check')
#         self.assertEqual(resolve(url).func,patientCheck)
    
#     def test_for_patient_create_resolves(self):
#         url = reverse('patient_records:patient_create')
#         self.assertEqual(resolve(url).func,patientCreate)

    
#     def test_for_patient_create_resolved(self):
#         url = reverse('patient_records:patient_create',args=['123'])
#         self.assertEqual(resolve(url).func,patientCreate)

    
#     def test_for_patient_details_resolves(self):
#         url = reverse('patient_records:patient_detail',args=['123'])
#         self.assertEqual(resolve(url).func,patientDetail)
    
#     def test_for_patient_details_resolved(self):
#         url = reverse('patient_records:patient_details')
#         self.assertEqual(resolve(url).func,patientDetails)


#     def test_for_patient_record_form_resolves(self):
#         url = reverse('patient_records:patient_record_form')
#         self.assertEqual(resolve(url).func,PatientView)

#     def test_for_patient_details_resolve(self):
#         url = reverse('patient_records:patient_record_list')
#         self.assertEqual(resolve(url).func,PatientList)



    

