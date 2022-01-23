from datetime import datetime
from django.test import TestCase
from patient_records.models import ProblemList,SocialHistory,Patient 

app_name = 'patient_records'
class SocialHistoryModelTest(TestCase): 
    
    def setUp(self):
        self.patient=Patient.objects.create(
            aadhaarId = 123123123123,
            name     = "jadoo",
            date_of_birth  = "2021-08-12",
            gender  ="Male"
        )

        

        self.patient_sh =  SocialHistory.objects.create(
           patient=self.patient,
           tobacco_smoking_status = "NEVER_SMOKED"  , 
           alcohol_consumption_status = "NEVER_DRINKED",
           alcohol_consumption_unit = 2,
           alcohol_consumption_frequency ="twice"
        )
    
    def test_it_has_information_fields(self):                  
       self.assertIsInstance(self.patient_sh.tobacco_smoking_status, str)
       self.assertIsInstance(self.patient_sh.alcohol_consumption_status, str)
       self.assertIsInstance(self.patient_sh.alcohol_consumption_unit, int)
       self.assertIsInstance(self.patient_sh. alcohol_consumption_frequency , str)
       
 
 
   # 2 for equality
    def test_patient_equals_fields(self):                  
       self.assertEqual(str(self.patient_sh.tobacco_smoking_status),"NEVER_SMOKED")
       self.assertEqual(str(self.patient_sh.alcohol_consumption_status),"NEVER_DRINKED")
       self.assertEqual((self.patient_sh.alcohol_consumption_unit),2)
       self.assertEqual(str(self.patient_sh. alcohol_consumption_frequency),"twice")
     
 
 
   # 3 for not equality.
    def test_patient_notequals_fields(self):                  
       self.assertEqual(str(self.patient_sh.tobacco_smoking_status),"Former Smoker")
       self.assertEqual(str(self.patient_sh.alcohol_consumption_status), "Current Drinker")
       self.assertEqual((self.patient_sh.alcohol_consumption_unit),3)
       self.assertEqual(str(self.patient_sh. alcohol_consumption_frequency),"once")
 