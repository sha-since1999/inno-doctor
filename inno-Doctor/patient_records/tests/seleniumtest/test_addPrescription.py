
from django.test import LiveServerTestCase
from selenium import webdriver

from selenium.webdriver.support.select import Select
import time

from selenium.webdriver import ActionChains
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class PatientTest(unittest.TestCase):
    # @classmethod
    def setUp(self):
        global selenium
        selenium = webdriver.Chrome("chromedriver")
        selenium.maximize_window()
        selenium.get('http://127.0.0.1:8000/')
       

    def test_check_patient(self):
        loginbuton=selenium.find_element_by_css_selector("#navigation > ul > li:nth-child(3) > a").click()
        # time.sleep(3)
        email="thor@gmail.com"
        password="thor@12345"
        putemail=selenium.find_element_by_id("id_email")
        putemail.send_keys(email)
        putpassword=selenium.find_element_by_id("id_password")
        putpassword.send_keys(password)
    # click on sign in
        sign=selenium.find_element_by_css_selector("body > div.card.card-body.blur.shadow-blur.mx-3.mx-md-4.mt-n6 > div > form > div.text-center > button").click()
        time.sleep(5)

        # click on check patient button.patient_check portion.
        button=selenium.find_element_by_name('ck_patient')
        selenium.execute_script("arguments[0].click();", button)
        
        #put id in box
        Aadharkey="923412347234"
       
        enter=selenium.find_element_by_name("aadhaarId")
        enter.send_keys('923412347234')
        enter.send_keys(Keys.ENTER)










        # From here eprescription starts.
        actual_url="http://127.0.0.1:8000/patient_records/patient-detail/923412347234"

        clickONeprescription=selenium.find_element_by_xpath("/html/body/div[2]/div/section[1]/div/div/div/div/ul/li[1]/a")
        selenium.execute_script("arguments[0].click();",clickONeprescription)

        #  New Medication Item - enter patient Details.

        MedicationItem="Medicine"
        Name="AntiMedi"
        Form="Tablets"
        Category="Drug"
        UnitofPrescription="2"
        BatchId="67982300"
        ExpiryDate="23/06/2026"
        DoseAmount="1"
        DoseDuration="6"
        DoseUnit="1"
        DoseFrequency="2"
        DoseInterval="2"
        DoseSpecificTiming="12:30"
        Route="Null"
        BodySite="Throat"

        MedItem=selenium.find_element_by_id("id_medicationitem_set-0-medication_item").send_keys(MedicationItem)

        NameofMed=selenium.find_element_by_id("id_medicationitem_set-0-name").send_keys(Name)

        MedForm=selenium.find_element_by_id("id_medicationitem_set-0-form").send_keys(Form)

        MedCategory=selenium.find_element_by_id("id_medicationitem_set-0-category").send_keys(Category)

        Medunitprescription=selenium.find_element_by_id("id_medicationitem_set-0-unit_of_prescription").send_keys(UnitofPrescription)
        MedBatch=selenium.find_element_by_id("id_medicationitem_set-0-batch_id").send_keys(BatchId)

        MedExpiry=selenium.find_element_by_id("id_medicationitem_set-0-expiry").send_keys(ExpiryDate)

        MedDoseAmount=selenium.find_element_by_id("id_medicationitem_set-0-dose_amount").send_keys(DoseAmount)

        MeddoseDuration=selenium.find_element_by_id("id_medicationitem_set-0-dose_duration").send_keys(DoseDuration)

        MedDoseUnit=selenium.find_element_by_id("id_medicationitem_set-0-dose_unit").send_keys(DoseUnit)

        MedFrequency=selenium.find_element_by_id("id_medicationitem_set-0-dose_frequency").send_keys(DoseFrequency)

        MedInterval=selenium.find_element_by_id("id_medicationitem_set-0-dose_interval").send_keys(DoseInterval)

        MedStiming=selenium.find_element_by_id("id_medicationitem_set-0-dose_specific_timing").send_keys(DoseSpecificTiming)

        MedRoute=selenium.find_element_by_id("id_medicationitem_set-0-route").send_keys(Route)

        MedBodySite=selenium.find_element_by_id("id_medicationitem_set-0-body_site").send_keys(BodySite)



        Submitbutton=selenium.find_element_by_css_selector("body > div.card.card-body.blur.shadow-blur.mx-3.mx-md-4.mt-n6 > div > form > div.text-center > button")
        selenium.execute_script("arguments[0].click();", Submitbutton)
        expected_url=selenium.current_url
        self.assertEqual(actual_url,expected_url)
        
        
    
        
      








  

   # @classmethod
    def tearDown(self):
        time.sleep(10)
        selenium.close()




if __name__ == "__main__":
    unittest.main()
