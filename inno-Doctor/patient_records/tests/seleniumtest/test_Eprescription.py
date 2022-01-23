from ast import Return
from typing import KeysView
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver import ActionChains
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
 
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
       email="sumantdhiman2@gmail.com"
       password="Jobs@123"
       putemail=selenium.find_element_by_id("id_email")
       putemail.send_keys(email)
       putpassword=selenium.find_element_by_id("id_password")
       putpassword.send_keys(password)
       # click on sign in
       sign=selenium.find_element_by_css_selector("body > div.card.card-body.blur.shadow-blur.mx-3.mx-md-4.mt-n6 > div > form > div.text-center > button").click()
       time.sleep(5)
 
       # click on check patient button
       button=selenium.find_element_by_name('ck_patient')
       selenium.execute_script("arguments[0].click();", button)
      
       #put id in box           
       Aadharkey="923412347234"
       enter=selenium.find_element_by_name("aadhaarId")
       enter.send_keys('923412347234')
       enter.send_keys(Keys.ENTER)
 
      
 
 
# @classmethod
   def tearDown(self):
       time.sleep(10)
       selenium.close()
 
 
 
 
if __name__ == "__main__":
   unittest.main()