import unittest
from unittest.case import expectedFailure
import HtmlTestRunner
from base import Baseconfig
from config import Configuration
import time

class CheckPatientEps(unittest.TestCase):


    def test_check_patient_eps(self):
        Baseconfig.driver.get(Configuration.BASE_URL)
        actual_url = 'http://0.0.0.0:8000/patient_records/patient_record_list/'
        Baseconfig.driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[4]/a').click()
        Baseconfig.driver.find_element_by_xpath('//*[@id="aadharid"]').send_keys('526578372398')
        Baseconfig.driver.find_element_by_name('bdate').send_keys('19012022')
        Baseconfig.driver.find_element_by_xpath('/html/body/div[2]/div/form/div[3]/button').click()
        time.sleep(5)
        expected_url = Baseconfig.driver.current_url
        self.assertEqual(actual_url,expected_url)
        # Baseconfig.driver.quit()

    def test_check_patient_eps_invalid(self):
        # Baseconfig.driver.get(Configuration.BASE_URL)
        actual_url = 'https://0.0.0.0:8000/patient_records/patient_record_list/'
        time.sleep(2)
        Baseconfig.driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[4]/a').click()
        time.sleep(2)
        Baseconfig.driver.find_element_by_xpath('//*[@id="aadharid"]').send_keys('526578372234')
        Baseconfig.driver.find_element_by_name('bdate').send_keys('19012022')
        Baseconfig.driver.find_element_by_xpath('/html/body/div[2]/div/form/div[3]/button').click()
        time.sleep(2)
        expected_url = Baseconfig.driver.current_url
        self.assertNotEqual(actual_url,expected_url)
        Baseconfig.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./test_dir'))