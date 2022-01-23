
import unittest
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner
from base import Baseconfig
from config import Configuration
import time
from selenium.webdriver.support.select import Select
class AddVitalSign(unittest.TestCase):

    def setUp(self):
        Baseconfig.driver.get(Configuration.BASE_URL)

        
    def test_add_vitalsign(self):

        actual_url='http://0.0.0.0:8000/patient_records/patient-detail/526578372398'
        Baseconfig.driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[3]/a').click()
        Baseconfig.driver.find_element_by_id('id_email').send_keys(Configuration.USER_EMAIL)
        time.sleep(3)
        Baseconfig.driver.find_element_by_id('id_password').send_keys(Configuration.USER_PASSWORD)
        Baseconfig.driver.find_element_by_xpath('//*[@id="rememberMe"]').click()
        time.sleep(3)
        button=Baseconfig.driver.find_element_by_id('doctor_signin')
        Baseconfig.driver.execute_script("arguments[0].click();", button)
        time.sleep(3)

        checkpatient=Baseconfig.driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[1]/a/p')
        Baseconfig.driver.execute_script("arguments[0].click();", checkpatient)
      
        element=Baseconfig.driver.find_element_by_name("aadhaarId")
        element.send_keys('526578372398')
        element.send_keys(Keys.ENTER)

        addvitalsign = Baseconfig.driver.find_element_by_xpath('/html/body/div[2]/div/section[1]/div/div/div/div/ul/li[3]/a')
        Baseconfig.driver.execute_script("arguments[0].click();", addvitalsign)
        time.sleep(5)
        Baseconfig.driver.find_element_by_name('body_weight').send_keys('56')
        Baseconfig.driver.find_element_by_name('height').send_keys('56')
        Baseconfig.driver.find_element_by_name('respiration_rate').send_keys('56')
        Baseconfig.driver.find_element_by_name('pulse_rate').send_keys('56')
        Baseconfig.driver.find_element_by_name('body_temperature').send_keys('56')
        Baseconfig.driver.find_element_by_name('head_circumference').send_keys('56')
        Baseconfig.driver.find_element_by_name('pulse_oximetry').send_keys('56')
        Baseconfig.driver.find_element_by_name('body_mass_index').send_keys('56')
        Baseconfig.driver.find_element_by_name('blood_pressure_systolic').send_keys('56')
        Baseconfig.driver.find_element_by_name('blood_pressure_diastolic').send_keys('56')
        button1=Baseconfig.driver.find_element_by_xpath('/html/body/div[2]/div/form/div[11]/button')
        Baseconfig.driver.execute_script("arguments[0].click();", button1)
        

        expected_url = Baseconfig.driver.current_url
        self.assertEqual(actual_url, expected_url)
        Baseconfig.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_dir'))