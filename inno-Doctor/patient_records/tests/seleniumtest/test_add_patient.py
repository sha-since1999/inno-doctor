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
       

    def test_doctor_login(self):
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
        


        # Add patient click
        clickonaddpatient=selenium.find_element_by_xpath('//*[@id="navigation"]/ul/li[2]/a/p').click()
        actual_url="http://127.0.0.1:8000/patient_records/patient-detail/923412347234"
        AadharNumber="923412347234"
        Name_of_patiet="Sammi"
        Dob="10/01/1994"
        AadharId=selenium.find_element_by_name("aadhaarId").send_keys(AadharNumber)
        Name=selenium.find_element_by_name("name").send_keys(Name_of_patiet)
        dateofbirth=selenium.find_element_by_name("date_of_birth").send_keys(Dob)
        select = Select(selenium.find_element_by_name("gender"))
        select.select_by_visible_text("Male")

        button = selenium.find_element_by_name("addpatient")
        selenium.execute_script("arguments[0].click();", button)
        time.sleep(2)







          # Not in use.

#         expected_url=selenium.current_url
#         self.assertEqual(actual_url,expected_url)
#         # element = selenium.find_elements_by_class_name('div[class*="btn bg-gradient-info w-40 my-4 mb-2 mx-1"]')
#         # selenium.execute_script("arguments[0].click();", element)
#         print("my page title=",selenium.title)
#         time.sleep(2)
#         # self.assertEqual(len(AadharNumber),self.MaxDigit)
#         # assert 'Lebron James' in selenium.page_source
    
















    # def test_patient_add(self):
	    # browser = self.selenium
	    # url = self.live_server_url + '/login'
	    # browser.get(url)
        # actual_url="http://127.0.0.1:8000/patient_records/patient-detail/923412347234"
        # AadharNumber="923412347234"
        # Name_of_patiet="Sam"
        # Dob="10/01/1998"
        # AadharId=selenium.find_element_by_name("aadhaarId").send_keys(AadharNumber)
        # Name=selenium.find_element_by_name("name").send_keys(Name_of_patiet)
        # dateofbirth=selenium.find_element_by_name("date_of_birth").send_keys(Dob)
        # select = Select(selenium.find_element_by_name("gender"))
        # select.select_by_visible_text("Male")
        # # AddPatient=selenium.find_element_by_name("addpatient").click()
         
        # button = selenium.find_element_by_name("addpatient")
        # selenium.execute_script("arguments[0].click();", button)
        # time.sleep(2)
        # expected_url=selenium.current_url
        # self.assertEqual(actual_url,expected_url)
        # # element = selenium.find_elements_by_class_name('div[class*="btn bg-gradient-info w-40 my-4 mb-2 mx-1"]')
        # # selenium.execute_script("arguments[0].click();", element)
        # print("my page title=",selenium.title)
        # time.sleep(2)
        # # self.assertEqual(len(AadharNumber),self.MaxDigit)
        # # assert 'Lebron James' in selenium.page_source
    


    # @classmethod
    def tearDown(self):
        time.sleep(10)
        selenium.close()




if __name__ == "__main__":
    unittest.main()
