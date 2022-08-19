import time
import unittest
from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_mainassignment.utilities.BaseClass import BaseClass


class Cart(unittest.TestCase):
    def __init__(self, driver):
        self.driver = driver

    #creating object of baseclass for accessing logging
    obj = BaseClass()
    log = obj.getlogger()

    #locators
    grocery_icon = (By.XPATH, "/html/body//img[@alt='Grocery']")
    grocery_item_1 = (By.XPATH, "/html/body//button[@class='_2KpZ6l _1vgE2o']")
    grocery_item_1_name = (By.XPATH, "/html/body//div[@class='_1AtVbE col-12-12']/div[@class='_3E8aIl U0FDpA']//div[@class='_37K3-p']/div[@class='_3YgSsQ']//div[@class='l0t3ZD _1EinRB']")
    grocery_item_2 = (By.XPATH, "/html/body//div[@class='_294fWd']/button")
    grocery_item_2_name = (By.XPATH, "/html/body//div[@class='_1AtVbE col-12-12']/div[@class='_3E8aIl U0FDpA']//div[@class='_37K3-p']/div[@class='_3YgSsQ ']//div[@class='l0t3ZD _1EinRB']")
    cart_icon = (By.XPATH, "/html/body//div[@class='YUhWwv']/a/span")
    cart_item_1 = (By.XPATH, "/html/body//div[@class='_1AtVbE col-12-12'][4]//div[@class='_-4o6jJ']/a")
    cart_item_2 = (By.XPATH, "/html/body//div[@class='_1AtVbE col-12-12'][3]//div[@class='_-4o6jJ']/a")
    pincode = (By.XPATH, "/html/body/div//form[@class='E9Z0B8 _209xbS']/input[@name='pincode']")
    cart_item_1_minus_icon = (By.XPATH, "//div[@class='_1AtVbE col-12-12'][3]//button[@class='_2KpZ6l _1s8W43 _37Ieie']")
    cart_item_2_minus_icon = (By.XPATH, "//div[@class='_1AtVbE col-12-12'][4]//button[@class='_2KpZ6l _1s8W43 _37Ieie']")

    #module for select grocery
    def select_grocery(self):
        try:
            # wait 10 seconds before looking for element
            #click grocery icon
            element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(Cart.grocery_icon))
            element.click()
            Cart.log.info("selecting grocery successfully")

        except (StaleElementReferenceException, TimeoutException):
            print("Failed to click in select grocery")

    #module for entering pincode
    def enter_pincode(self):
        try:
            # wait 10 seconds before looking for element
            #enter pincode and hit Enter
            element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(Cart.pincode))
            element.send_keys("603203")

            element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(Cart.pincode))
            element.send_keys(Keys.ENTER)
            Cart.log.info("enter pincode successfully")

        except (StaleElementReferenceException, TimeoutException):
            print("Failed to click in enter pincode")

    #module for adding items in cart
    def add_items_in_cart(self):
        #declaring global variables for storing items name
        global item_1_name, item_2_name

        try:
            # wait 10 seconds before looking for element
            #click/select grocery item 1
            element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(Cart.grocery_item_1))
            element.click()

            # storing item 1 name
            element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(Cart.grocery_item_1_name))
            item_1_name = element.text
            print("grocery item 1: ", item_1_name)

            time.sleep(5)
            # storing item 1 name
            element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(Cart.grocery_item_2_name))
            item_2_name = element.text
            print("grocery item 2: ", item_2_name)

            # click/select grocery item 2
            element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(Cart.grocery_item_2))
            element.click()

            Cart.log.info("adding items in cart successfull")

        except (StaleElementReferenceException, TimeoutException):
            print("Failed to click in add items in cart")

    #module for verifying items in cart
    def verify_items_in_cart(self):
        try:
            # wait 10 seconds before looking for element
            #click on cart icon
            element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(Cart.cart_icon))
            element.click()

            #storing name of cart item 1
            element = WebDriverWait(self.driver, 25).until(
                EC.presence_of_element_located(Cart.cart_item_1))
            cart_item_1_name = element.text
            print("cart item 1: ", cart_item_1_name)

            # storing name of cart item 2
            element = WebDriverWait(self.driver, 25).until(
                EC.presence_of_element_located(Cart.cart_item_2))
            cart_item_2_name = element.text
            print("cart item 2: ", cart_item_2_name)


            #verification through assertion of results matching
            self.assertIn(item_1_name, cart_item_1_name)
            self.assertIn(item_2_name, cart_item_2_name)

            if item_1_name in cart_item_1_name and item_2_name in cart_item_2_name:
                print("items verified")


        except (StaleElementReferenceException, TimeoutException):
            print("Failed to click in verify items in cart")









