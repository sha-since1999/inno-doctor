import unittest
from unittest.case import expectedFailure
import HtmlTestRunner
from base import Baseconfig
from config import Configuration
import time

class CheckPatient(unittest.TestCase):
     def test_check_patient(self):
         Baseconfig.driver.find_element_by_xpath('//*[@id="search-input"]').send_keys('123456789')
         Baseconfig.driver.find_element_by_xpath('/html/body/div/div/form/label/input[2]').click()