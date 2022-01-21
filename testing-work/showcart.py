import unittest
from unittest.case import expectedFailure
import HtmlTestRunner
from base import Baseconfig
from config import Configuration
from login import Login
import time
from add_to_cart import AddToCart

class ShowCart(unittest.TestCase):
    def test_show_cart(self):
        AddToCart.test_cart(self)
        Baseconfig.driver.find_element_by_id('add-to-cart-sauce-labs-bike-light').click()
        time.sleep(3)
        Baseconfig.driver.find_element_by_id('add-to-cart-sauce-labs-bolt-t-shirt').click()
        time.sleep(3)
        Baseconfig.driver.find_element_by_xpath('//*[@id="shopping_cart_container"]/a').click()
        time.sleep(3)
        Baseconfig.driver.find_element_by_id('checkout').click()
        time.sleep(3)
        Baseconfig.driver.find_element_by_id('react-burger-menu-btn').click()
        time.sleep(3)
        Baseconfig.driver.find_element_by_xpath('//*[@id="logout_sidebar_link"]').click()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))