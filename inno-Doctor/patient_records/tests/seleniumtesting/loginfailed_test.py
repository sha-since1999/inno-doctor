
import unittest
from unittest.case import expectedFailure
import HtmlTestRunner
from base import Baseconfig
from config import Configuration
import time
class Login(unittest.TestCase):

    def setUp(self):
        Baseconfig.driver.get(Configuration.BASE_URL)

        
    def test_doctor_login_failed(self):
        actual_url = 'http://0.0.0.0:8000/'
        Baseconfig.driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[3]/a').click()
        Baseconfig.driver.find_element_by_id('id_email').send_keys(Configuration.INVALID_USER_EMAIL)
        Baseconfig.driver.find_element_by_id('id_password').send_keys(Configuration.INVALID_USER_PASSWORD)
        Baseconfig.driver.find_element_by_xpath('//*[@id="rememberMe"]').click()
        time.sleep(3)
        button=Baseconfig.driver.find_element_by_id('doctor_signin')
        Baseconfig.driver.execute_script("arguments[0].click();", button)
        expectedUrl= Baseconfig.driver.current_url
        self.assertNotEqual(actual_url,expectedUrl)
        time.sleep(2)
        Baseconfig.driver.quit()

    
    
    
   
      


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_dir'))