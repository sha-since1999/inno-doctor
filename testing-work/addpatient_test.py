from lib2to3.pgen2 import driver
import unittest
from unittest.case import expectedFailure
import HtmlTestRunner
from base import Baseconfig
from config import Configuration
import time
from selenium.webdriver.support.select import Select
class AddPatient(unittest.TestCase):

    def setUp(self):
        Baseconfig.driver.get(Configuration.BASE_URL)

        
    def test_add_patient(self):
        actual_url = 'http://0.0.0.0:8000/patient_records/patient-detail/923412347235'
        Baseconfig.driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[3]/a').click()
        Baseconfig.driver.find_element_by_id('id_email').send_keys(Configuration.USER_EMAIL)
        time.sleep(3)
        Baseconfig.driver.find_element_by_id('id_password').send_keys(Configuration.USER_PASSWORD)
        Baseconfig.driver.find_element_by_xpath('//*[@id="rememberMe"]').click()
        time.sleep(3)
        button=Baseconfig.driver.find_element_by_id('doctor_signin')
        Baseconfig.driver.execute_script("arguments[0].click();", button)
        time.sleep(3)
        Baseconfig.driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[2]/a/p').click()
        AadharNumber="923412347239"
        Name_of_patiet="Sam"
        Dob="10/01/1998"
        Baseconfig.driver.find_element_by_name("aadhaarId").send_keys(AadharNumber)
        Baseconfig.driver.find_element_by_name("name").send_keys(Name_of_patiet)
        Baseconfig.driver.find_element_by_name("date_of_birth").send_keys(Dob)
        select = Select(Baseconfig.driver.find_element_by_name("gender"))
        select.select_by_visible_text("Male")
        button=Baseconfig.driver.find_element_by_name('addpatient')
        Baseconfig.driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
    
        expected_url=Baseconfig.driver.current_url
        self.assertEqual(actual_url,expected_url)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_dir'))