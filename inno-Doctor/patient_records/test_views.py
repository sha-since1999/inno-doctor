# from django.http import response
# from django.test import TestCase, Client
# from django.urls import reverse, resolve
# from accounts.models import Activation
# import json


# class TestViews(TestCase):

#     def setUp(self):
#         self.client = Client()

#     def test_problemlist(self):
#         response=self.client.get(reverse('patient_records:patient_problem_list_create'),args=['123'])
#         self.assertEqual(response.status_code,200)