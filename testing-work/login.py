import unittest
from unittest.case import expectedFailure
import HtmlTestRunner
from base import Baseconfig
from config import Configuration
import time
class Login(unittest.TestCase):
    def test_do_login(self):
        Baseconfig.driver.find_element_by_xpath('/html/body/div/a[1]').click()
        Baseconfig.driver.find_element_by_xpath('//*[@id="id_email_or_username"]').send_keys(Configuration.USER_NAME)
        Baseconfig.driver.find_element_by_xpath('//*[@id="id_password"]').send_keys(Configuration.USER_PASSWORD)
        Baseconfig.driver.find_element_by_xpath('/html/body/div/div/form/button').click()
    
    @expectedFailure
    def test_fail_login(self):
        Baseconfig.driver.find_element_by_xpath('/html/body/div/a[1]').click()
        Baseconfig.driver.find_element_by_xpath('//*[@id="id_email_or_username"]').send_keys(Configuration.INVALID_USER_NAME)
        Baseconfig.driver.find_element_by_xpath('//*[@id="id_password"]').send_keys(Configuration.INVALID_PASSWORD)
        Baseconfig.driver.find_element_by_xpath('/html/body/div/div/form/button').click()
      


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))