import unittest
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner
from base import Baseconfig
from config import Configuration
import time
from selenium.webdriver.support.select import Select
class AddEprescription(unittest.TestCase):

    def setUp(self):
        Baseconfig.driver.get(Configuration.BASE_URL)

        
    def test_add_eprescription(self):

        actual_url='http://0.0.0.0:8000/patient_records/patient-detail/923412347235'
        Baseconfig.driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[3]/a').click()
        Baseconfig.driver.find_element_by_id('id_email').send_keys(Configuration.USER_EMAIL)
        time.sleep(3)
        Baseconfig.driver.find_element_by_id('id_password').send_keys(Configuration.USER_PASSWORD)
        Baseconfig.driver.find_element_by_xpath('//*[@id="rememberMe"]').click()
        time.sleep(3)
        button=Baseconfig.driver.find_element_by_id('doctor_signin')
        Baseconfig.driver.execute_script("arguments[0].click();", button)
        time.sleep(3)

        checkpatient=Baseconfig.driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[1]/a/p')
        Baseconfig.driver.execute_script("arguments[0].click();", checkpatient)
      
        element=Baseconfig.driver.find_element_by_name("aadhaarId")
        element.send_keys('923412347235')
        element.send_keys(Keys.ENTER)
        time.sleep(3)
        clickONeprescription=Baseconfig.driver.find_element_by_xpath("/html/body/div[2]/div/section[1]/div/div/div/div/ul/li[1]/a")
        Baseconfig.driver.execute_script("arguments[0].click();",clickONeprescription)
    
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
    
        Baseconfig.driver.find_element_by_id("id_medicationitem_set-0-medication_item").send_keys(MedicationItem)
    
        Baseconfig.driver.find_element_by_id("id_medicationitem_set-0-name").send_keys(Name)
    
        Baseconfig.driver.find_element_by_id("id_medicationitem_set-0-form").send_keys(Form)
    
        Baseconfig.driver.find_element_by_id("id_medicationitem_set-0-category").send_keys(Category)
    
        Baseconfig.driver.find_element_by_id("id_medicationitem_set-0-unit_of_prescription").send_keys(UnitofPrescription)
        Baseconfig.driver.find_element_by_id("id_medicationitem_set-0-batch_id").send_keys(BatchId)
    
        Baseconfig.driver.find_element_by_id("id_medicationitem_set-0-expiry").send_keys(ExpiryDate)
    
        Baseconfig.driver.find_element_by_id("id_medicationitem_set-0-dose_amount").send_keys(DoseAmount)
    
        Baseconfig.driver.find_element_by_id("id_medicationitem_set-0-dose_duration").send_keys(DoseDuration)
    
        Baseconfig.driver.find_element_by_id("id_medicationitem_set-0-dose_unit").send_keys(DoseUnit)
    
        Baseconfig.driver.find_element_by_id("id_medicationitem_set-0-dose_frequency").send_keys(DoseFrequency)
    
        Baseconfig.driver.find_element_by_id("id_medicationitem_set-0-dose_interval").send_keys(DoseInterval)
    
        Baseconfig.driver.find_element_by_id("id_medicationitem_set-0-dose_specific_timing").send_keys(DoseSpecificTiming)
    
        Baseconfig.driver.find_element_by_id("id_medicationitem_set-0-route").send_keys(Route)
    
        Baseconfig.driver.find_element_by_id("id_medicationitem_set-0-body_site").send_keys(BodySite)
    
    
    
        Submitbutton=Baseconfig.driver.find_element_by_css_selector("body > div.card.card-body.blur.shadow-blur.mx-3.mx-md-4.mt-n6 > div > form > div.text-center > button")
        Baseconfig.driver.execute_script("arguments[0].click();", Submitbutton)
        expected_url=Baseconfig.driver.current_url
        self.assertEqual(actual_url,expected_url)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_dir'))