from datetime import datetime
from django.test import TestCase
from patient_records.models import ProblemList,SocialHistory,Patient 


app_name = 'patient_records'
class ProblemListModelTest(TestCase): 
     
    def setUp(self):
        
        self.patient=Patient.objects.create(
            aadhaarId = 123123123123,
            name     = "jadoo",
            date_of_birth  = "2021-08-12",
            gender  ="Male"
        )

 
        
        self.patients = ProblemList.objects.create(
        patient=self.patient,
        problem ="corona",
        body_site = "lungs",
        severity = "Mild",
        abatement_date = "2027-06-12",
        diagnostic_certainty = "confirm"
      
        )

        #    self.patients.save()
 
    # (1) this is the first case.
    def test_it_has_information_fields(self):                  
       self.assertIsInstance(self.patients.problem, str)
       self.assertIsInstance(self.patients.body_site, str)
       self.assertIsInstance(self.patients.severity, str)
       self.assertIsInstance(self.patients.abatement_date, str)
       self.assertIsInstance(self.patients.diagnostic_certainty, str)
 
 
    # 2 for equality
    def test_patient_equals_fields(self):                  
       self.assertEqual(str(self.patients.problem),"corona")
       self.assertEqual(str(self.patients.body_site),"lungs")
       self.assertEqual(str(self.patients.severity),"Mild")
       self.assertEqual(str(self.patients.abatement_date),"2027-06-12")
       self.assertEqual(str(self.patients.diagnostic_certainty),"confirm")
 
 
   # 3 for not equality.
    def test_patient_notequals_fields(self):                  
       self.assertNotEqual(str(self.patients.body_site),"throat")
       self.assertNotEqual(str(self.patients.severity),"intense")
       self.assertNotEqual(str(self.patients.abatement_date),"2027-06-11")
       self.assertNotEqual(str(self.patients.diagnostic_certainty),"unsure")
