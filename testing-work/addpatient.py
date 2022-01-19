import unittest
from unittest.case import expectedFailure
import HtmlTestRunner
from base import Baseconfig
from config import Configuration
import time
class AddPatientTest(unittest.TestCase):
    def test_add_patient(self):
         Baseconfig.driver.find_element_by_xpath('//*[@id="id_aadhaarId"]').send_keys('123456789')
         Baseconfig.driver.find_element_by_xpath('//*[@id="id_name"]').send_keys('Rishab')
         Baseconfig.driver.find_element_by_xpath('//*[@id="id_date_of_birth"]').send_keys('2022-01-01')
         time.sleep(1)
         Baseconfig.driver.find_element_by_xpath('//*[@id="id_gender"]/option[2]').click()
         time.sleep(3)
         Baseconfig.driver.find_element_by_xpath('/html/body/div/div/div/form/button').click()
         time.sleep(3)
         Baseconfig.driver.close()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))