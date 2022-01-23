from http.client import responses
from pydoc import resolve
from django.test import TestCase , Client
from django.urls import reverse
from patient_records.models import *
import json

class PatientTestViews(TestCase):
    def setUp(self) :
        self.client= Client()
        self.details_url= reverse('patient_records:patient_details')
        self.detail_url = reverse('patient_records:patient_detail',args=['123412341234'])
        self.check_url =  reverse('patient_records:patient_check')
        
        self.patient1= Patient.objects.create(
            aadhaarId          = 123412341234,
            name                 = 'unknown',
            date_of_birth    = '2020-01-10',
            gender               = 'M',
        )
        
    def test_patient_details_POST_view(self):
        response= self.client.post(self.details_url, { 'aadhaarId':123412341234})
        
        self.assertEqual(response.status_code,200)
        self.assertEqual(self.patient1.aadhaarId,123412341234)
        self.assertTemplateUsed(response, "patient_records/patient-details.html")
    
    def test_patient_details_POST_with_no_data_view(self):
        response= self.client.post(self.details_url)
        
        self.assertEqual(response.status_code,302)
        
    def test_patient_detail_view(self):
        response= self.client.get(self.detail_url, { 'aadhaarId':123412341234})
        
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, "patient_records/patient-details.html")

    def test_patietn_check(self):
        url= reverse('patient_records:patient_check')
        response= self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_patient_create(self):
        url= reverse('patient_records:patient_create')
        response= self.client.post(url, {
            'aadhaarId'          : '97869876987',
            'name'                 : 'rohit',
            'date_of_birth'    :'2020-01-10',
            'gender'               : 'M'
        })
        patient2= Patient.objects.get(aadhaarId='97869876987')
        
        self.assertEqual(patient2.name,'rohit')
        self.assertEqual(patient2.gender,'M')
        
    def test_patient_update(self):
        url= reverse('patient_records:patient_create')
        response= self.client.post(url, {
            'aadhaarId'          :'97869876987',
            'name'                 : 'geeta',
            'date_of_birth'    :'2020-01-10',
            'gender'               : 'F',
        })
        patient2= Patient.objects.get(aadhaarId='97869876987')
        
        self.assertEqual(patient2.name,'geeta')
        self.assertEqual(patient2.gender,'F')
    




        
