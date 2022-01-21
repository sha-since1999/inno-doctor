from ast import arg
from django.http import response
from django.test import TestCase, Client
from django.urls import reverse, resolve
from patient_records.models import Patient,ProblemList,VitalSign,SocialHistory
import json

### test_views.py

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()


    # patient check.
    def test_patientcheck_view(self):
        response = self.client.get(reverse('patient_records:patient_check'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'patient_records/patient-check.html')
    
    # patient check details.
    def test_check_patient_details_view(self):
        response = self.client.get(reverse('patient_records:patient_details'),follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'patient_records/patient-check.html')


    # patient create.
    def test_patientCreate_view(self):
        response = self.client.get(reverse('patient_records:patient_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'patient_records/patient-create.html')

    # patient create.
    def test_patient_create(self):
        url= reverse('patient_records:patient_create')
        response= self.client.post(url, {
            'aadhaarId'          : '432143214321',
            'name'                 : 'Hulk',
            'date_of_birth'    :'1996-01-10',
            'gender'               : 'M'
        })
        patient2= Patient.objects.get(aadhaarId='432143214321')
        
        self.assertEqual(patient2.name,'Hulk')
        self.assertEqual(patient2.gender,'M')



    # patient update
    def test_patient_update(self):
        url= reverse('patient_records:patient_create')
        response= self.client.post(url, {
            'aadhaarId'          :'123412341234',
            'name'                 : 'Samy',
            'date_of_birth'    :'2020-01-10',
            'gender'               : 'F',
        })
        patient2= Patient.objects.get(aadhaarId='123412341234')
        self.assertEqual(patient2.name,'Samy')
        self.assertEqual(patient2.gender,'F')




























































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

    