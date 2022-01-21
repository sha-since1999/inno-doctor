
# app_name = 'patient_records'

# from datetime import datetime
# from django.test import TestCase

# from patient_records.models import Patient,ProblemList

# # (a) 
# class patientModelTest(TestCase):  

#     # (b)  we create a single patient instance to be used by the rest of the test methods.
#     @classmethod
#     def setUpTestData(cls):                                     
#         cls.patient = Patient.objects.create(
#             name="John", 
#             aadhaarId="12345",
#             date_of_birth="1997-06-12",
#             gender="Male"
#         ) 
    
#     # (1) this is first case.
#     def test_it_has_information_fields(self):                   
#         self.assertIsInstance(self.patient.name, str)
#         self.assertIsInstance(self.patient.aadhaarId, str)
#         self.assertIsInstance(self.patient.date_of_birth, str)
#         self.assertIsInstance(self.patient.gender, str)

#     # 2 for equality
#     def test_patient_equals_fields(self):                   
#         self.assertEqual(str(self.patient.name),'John')
#         self.assertEqual(str(self.patient.aadhaarId),'12345')
#         self.assertEqual(str(self.patient.gender),'Male')


#     # 3 for not equality.
#     def test_patient_notequals_fields(self):                   
#         self.assertEqual(str(self.patient.name),'cena')
#         self.assertEqual(str(self.patient.aadhaarId),'123456')
#         self.assertEqual(str(self.patient.gender),'FeMale')

#     # 4
#     def test_it_has_timestamps(self):                           
#         self.assertIsInstance(self.patient.last_udpated_on, datetime)

























# app_name = 'patient_records'
# from datetime import datetime
# from django.test import TestCase
# from patient_records.models import Patient, ProblemList
# (a)
# class patientModelTest(TestCase):
  # (b)  we create a single patient instance to be used by the rest of the test methods.
#   @classmethod
#   def setUpTestData(cls):                                   
    #   cls.patients = ProblemList.objects.create(
    #       problem ="corona",
    #       body_site = "lungs",
    #       onset_date = "2021-06-12",
    #       abatement_date = "2027-06-12",
    #       diagnostic_certainty = "confirm",
    #       severity="high"
    #   )
#    # (1) this is the first case.
#    def test_it_has_information_fields(self):                 
#        self.assertIsInstance(self.patient.problem, str)
#        self.assertIsInstance(self.patient.adhaarId, str)
#        self.assertIsInstance(self.patient.date_of_birth, str)
#        self.assertIsInstance(self.patient.gender, str)
  # 2 for equality
    # def test_patient_equals_fields(self):                 
    #     self.assertEqual(str(self.patients.problem),'corona')
    #     self.assertEqual(str(self.patients.body_site),'lungs')
    #     self.assertEqual(str(self.patients.onset_date),"2021-06-12")
    #     self.assertEqual(str(self.patients.abatement_date),"2027-06-12")
    #     self.assertEqual(str(self.patients.diagnostic_certainty),"confirm")






























































# class PatientModelTest(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         # Set up non-modified objects used by all test methods
#         patientCreate.objects.create(name='Batman')

#     def test_aadhaarId(self):
#         author = patientCreate.objects.get(aadhaarId=123412341234)
#         field_label = author._meta.get_field('aadhaarId').verbose_name
#         self.assertEqual(field_label, 'aadhaarId')



#     def test_first_name_label(self):
#         author = patientCreate.objects.get(aadhaarId=1)
#         field_label = author._meta.get_field('name').verbose_name
#         self.assertEqual(field_label, 'name')


#     def test_first_name_max_length(self):
#         author = patientCreate.objects.get(aadhaarId=1)
#         max_length = author._meta.get_field('name').max_length
#         self.assertEqual(max_length, 100)



#     def test_date_of_birth(self):
#         author = patientCreate.objects.get(aadhaarId=1)
#         field_label = author._meta.get_field('date_of_birth').verbose_name
#         self.assertEqual(field_label, 'date_of_birth')


#     def test_get_absolute_url(self):
#         author = patientCreate.objects.get(aadhaarId=1)
#         # This will also fail if the urlconf is not defined.
#         self.assertEqual(author.get_absolute_url(), '/patient_records/patientCreate/1')



# test_models.py

# class PatientModelTestcase(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         Patient.objects.create(aadhaarId ="123412341234",name="John",date_of_birth=10/12/1998,gender="Male")

#     def test_string_method(self):
#         patient= Patient.objects.get(aadhaarId=1)
#         expected_string = f"Name:{patient.name} {patient.aadhaarId} {patient.date_of_birth} {patient.gender}"
#         self.assertEqual(str(patient), expected_string)

#     def test_get_absolute_url(self):
#         patient = Patient.objects.get(id=1)
#         self.assertEqual(patient.get_absolute_url(), "/patient-create/1")


