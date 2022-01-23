from django.test import LiveServerTestCase
from selenium import webdriver

from selenium.webdriver.support.select import Select
import time

from selenium.webdriver import ActionChains
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

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
        email="thor@gmail.com"
        password="thor@12345"
        putemail=selenium.find_element_by_id("id_email")
        putemail.send_keys(email)
        putpassword=selenium.find_element_by_id("id_password")
        putpassword.send_keys(password)
    # click on sign in
        sign=selenium.find_element_by_css_selector("body > div.card.card-body.blur.shadow-blur.mx-3.mx-md-4.mt-n6 > div > form > div.text-center > button").click()
        time.sleep(5)

        # click on check patient button.patient_check portion.
        button=selenium.find_element_by_name('ck_patient')
        selenium.execute_script("arguments[0].click();", button)
        
        #put id in box
        Aadharkey="923412347234"
       
        enter=selenium.find_element_by_name("aadhaarId")
        enter.send_keys('923412347234')
        enter.send_keys(Keys.ENTER)



# Social History Start fro mere.

        actual_url="http://127.0.0.1:8000/patient_records/patient-detail/923412347234"

        clickONeprescription=selenium.find_element_by_xpath("/html/body/div[2]/div/section[1]/div/div/div/div/ul/li[4]/a")
        selenium.execute_script("arguments[0].click();",clickONeprescription)

 # select options
        TobaccoSmokingStatusselect = Select(selenium.find_element_by_name("tobacco_smoking_status"))
        TobaccoSmokingStatusselect.select_by_visible_text("Current Smoker")

        AlcoholConsumptionStatuselect = Select(selenium.find_element_by_name("alcohol_consumption_status"))
        AlcoholConsumptionStatuselect.select_by_visible_text("Current Drinker")

        AlcoholConsumptionUnit=selenium.find_element_by_id("id_alcohol_consumption_unit").send_keys("4")

        AlcoholConsumptionFrequency=selenium.find_element_by_id("id_alcohol_consumption_frequency").send_keys("5")

        Submitbutton=selenium.find_element_by_css_selector("body > div.card.card-body.blur.shadow-blur.mx-3.mx-md-4.mt-n6 > div > form > div.text-center > button")
        selenium.execute_script("arguments[0].click();", Submitbutton)
        expected_url=selenium.current_url
        self.assertEqual(actual_url,expected_url)
        














   # @classmethod
    def tearDown(self):
        time.sleep(10)
        selenium.close()




if __name__ == "__main__":
    unittest.main()
