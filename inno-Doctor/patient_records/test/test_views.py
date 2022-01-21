# from django.http import response
# from django.test import TestCase, Client
# from django.urls import reverse, resolve
# from patient_records.models import Patient,ProblemList,VitalSign,SocialHistory
# import json

# ### test_views.py

# class TestViews(TestCase):

#     def setUp(self):
#         self.client = Client()

#     def test_patientcheck_view(self):
#         response = self.client.get(reverse('patient_records:patient_check'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'patient_records/patient-check.html')
    
#     def test_patientCreate_view(self):
#         response = self.client.get(reverse('patient_records:patient_create'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'patient_records/patient-create.html')

#     def test_check_patient_details_view(self):
#         response = self.client.get(reverse('patient_records:patient_details'))
#         self.assertEqual(response.status_code, 302)
#         self.assertTemplateUsed(response, 'patient_records/patient-details.html')

    
#     def test_check_patient_detail_view(self):
#         response = self.client.get(reverse('patient_records:patient_detail'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'patient_records/patient-details.html')






























































# class PatientListViewTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         number_of_patients = 30
#         for adhaarId_id in range(number_of_patients):
#             Patient.objects.create(name=f"John{adhaarId_id}")

    # def test_url_exists(self):
    #     response = self.client.get("/patient-create")
    #     self.assertEqual(response.status_code, 200)

    # def test_url_accessible_by_name(self):
    #     response = self.client.get(reverse('patient-create'))
    #     self.assertEqual(response.status_code, 200)

    # def test_view_uses_correct_template(self):
    #     response = self.client.get(reverse('patient-create'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'templates/patient-create.html')

    