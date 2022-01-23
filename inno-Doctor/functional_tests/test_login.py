from lib2to3.pgen2 import driver
import unittest
from unittest.case import expectedFailure
import HtmlTestRunner
from base import Baseconfig
from config import Configuration
import time
class Login(unittest.TestCase):

    def setUp(self):
        Baseconfig.driver.get(Configuration.BASE_URL)

        
    def test_doctor_login_(self):
        actual_url = 'http://0.0.0.0:8000/'
        Baseconfig.driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[3]/a').click()
        Baseconfig.driver.find_element_by_id('id_email').send_keys(Configuration.USER_EMAIL)
        time.sleep(3)
        Baseconfig.driver.find_element_by_id('id_password').send_keys(Configuration.USER_PASSWORD)
        Baseconfig.driver.find_element_by_xpath('//*[@id="rememberMe"]').click()
        time.sleep(3)
        button=Baseconfig.driver.find_element_by_id('doctor_signin')
        Baseconfig.driver.execute_script("arguments[0].click();", button)
        time.sleep(3)
        expectedUrl= Baseconfig.driver.current_url
        time.sleep(4)
        self.assertEqual(actual_url,expectedUrl)
        Baseconfig.driver.quit()

    
    
   



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_dir'))