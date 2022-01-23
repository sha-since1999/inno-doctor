# from django.test import LiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
# import time
# from selenium.webdriver import ActionChains
# import unittest
# # from HTMLTestRunner import HTMLTestRunner
 
 
 
# # Create your tests here. Opening home page.
# class PatientTest(unittest.TestCase):
 
#     def setUp(self):
#        global selenium
#        selenium = webdriver.Chrome("/home/sumant/Downloads/chromedriver")
#        selenium.maximize_window()
#        selenium.get('http://127.0.0.1:8000')
 
  
#     def test_git(self):
#        # actual_url="https://github.com/sha-since1999/inno-doctor"
#        gitlink=selenium.find_element_by_css_selector("#navigation > ul > li:nth-child(1) > a > p")
#        gitlink.click()
#        # excepted_url=selenium.current_url
#        # self.assertEqual(actual_url,excepted_url)
#        time.sleep(2)
#        selenium.quit()

 
 
#     #                          # 2.Testing change language.
 
#     # def test_language(self):
#     #    lanuguages=selenium.find_element_by_css_selector("#navigation > ul > li:nth-child(2) > a > p")
#     #    lanuguages.click()
#     # #. Click on the dropdown and select the option Russian (ru)
#     #    select = Select(selenium.find_element_by_name("language"))
#     #    select.select_by_visible_text("Russian (ru)")
#     #    clickchange = selenium.find_element_by_css_selector("body > div.card.card-body.blur.shadow-blur.mx-3.mx-md-4.mt-n6 > div > form > div.text-center > button").click()
#     #    time.sleep(5)
#     #    selenium.quit()
 
 
 
#    #                     3      Doctor Login.
 
#     # def test_doctor_login(self):
#     #    loginbuton=selenium.find_element_by_css_selector("#navigation > ul > li:nth-child(3) > a").click()
#     #    email="thor@gmail.com"
#     #    password="thor@12345"
#     #    putemail=selenium.find_element_by_id("id_email")
#     #    putemail.send_keys(email)
#     #    putpassword=selenium.find_element_by_id("id_password")
#     #    putpassword.send_keys(password)
#     #    # click on sign in
#     #    sign=selenium.find_element_by_css_selector("body > div.card.card-body.blur.shadow-blur.mx-3.mx-md-4.mt-n6 > div > form > div.text-center > button").click()
#     #    time.sleep(5)
#     #    selenium.quit()
 
 
#    #                  4       Continue as Patient
#     # def test_doctor_login(self):
#     #    patient=selenium.find_element_by_css_selector("#navigation > ul > li:nth-child(4) > a").click()
#     #    aadharid=123412341234
#     #    dateofbirth="10/01/1998"
#     #    putId=selenium.find_element_by_name("aadharid").send_keys(aadharid)
#     #    putdob=selenium.find_element_by_name("bdate").send_keys(dateofbirth)
#     #    SeeRecord=selenium.find_element_by_class_name("body > div.card.card-body.blur.shadow-blur.mx-3.mx-md-4.mt-n6 > div > form > div.text-center > button").click()
#     #    time.sleep(5)
 
 
# # mytest=PlayerFormTest()
# # mytest.testform()

#        def tearDown(self):
#            time.sleep(10)
#            selenium.close()
 
 
 
# if __name__ == "__main__":
#    unittest.main()
 
 
 
 
 
 
 
