from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver import ActionChains
import unittest


class PatientTest(unittest.TestCase):

    def test_patient_add(self):
	    # browser = self.selenium
	    # url = self.live_server_url + '/login'
	    # browser.get(url)
        selenium = webdriver.Chrome("chromedriver")
        selenium.maximize_window() 
        selenium.get('http://127.0.0.1:8000/patient_records/patient-create/')
        AadharNumber=432143214321
        Name_of_patiet="Samuel"
        Dob="10/01/1998"
        AadharId=selenium.find_element_by_name("aadhaarId").send_keys(AadharNumber)
        Name=selenium.find_element_by_name("name").send_keys(Name_of_patiet)
        dateofbirth=selenium.find_element_by_name("date_of_birth").send_keys(Dob)
        select = Select(selenium.find_element_by_name("gender"))
        select.select_by_visible_text("Male")
        AddPatient=selenium.find_element_by_css_selector("body > div.card.card-body.blur.shadow-blur.mx-3.mx-md-4.mt-n6 > div > form > div.text-center > button").click()
        time.sleep(5)








	    










if __name__ == "__main__":
    unittest.main()
