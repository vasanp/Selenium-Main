import unittest
from selenium.common import StaleElementReferenceException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_mainassignment.utilities.BaseClass import BaseClass


class WishList(unittest.TestCase):
    def __init__(self, driver):
        self.driver = driver

    # creating object for baseclass to access logging functions
    obj = BaseClass()
    log = obj.getlogger()

    #locators
    fashion_icon = (By.XPATH, "/html/body//img[@alt='Fashion']")
    fashion_dropdown = (By.XPATH, "/html/body/div//div[@class='_1psGvi SLyWEo']//div[@class='ZEl_b_ _3joddx _2ogGYG _23xUYh _3pAV4E']/div[@class='_3_Fivj']//a")
    fashion_item_1 = (By.XPATH, "/html/body/div//div[@class='_13oc-S']/div[1]//div[@class='_36FSn5']")
    fashion_item_1_name = (By.XPATH, "/html/body/div//div[@class='_13oc-S']/div[1]//div[@class='_2WkVRV']")
    fashion_item_2 = (By.XPATH, "/html/body/div//div[@class='_13oc-S']/div[2]//div[@class='_36FSn5']")
    fashion_item_2_name = (By.XPATH, "/html/body/div//div[@class='_13oc-S']/div[2]//div[@class='_2WkVRV']")
    my_account = (By.XPATH, "/html/body/div/div//div[@class='_28p97w']/div")
    wishlist = (By.XPATH,
                     "/html/body//div[@class='ZEl_b_ _1J9ow0 _2ogGYG _23xUYh _3pAV4E']//div[@class='_3_Fivj']/div[@class='_1bQ5Pp']/ul[@class='pO9syL undefined']/li[5]")

    wishlist_item_1_name = (By.XPATH, "/html/body/div//div[@class='_3E8aIl sTQ7AV']//div[@class='_1M-Ete'][1]//div[@class='_3hscEA']")
    wishlist_item_2_name = (By.XPATH, "/html/body/div//div[@class='_3E8aIl sTQ7AV']//div[@class='_1M-Ete'][2]//div[@class='_3hscEA']")

   #module for searching fashion items
    def search_fashion_items(self):
        #creating object of actions class
        a = ActionChains(self.driver)
        try:
            #click on fashion icon
            element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(WishList.fashion_icon))


        except (StaleElementReferenceException, TimeoutException, ElementClickInterceptedException):
            print("Failed to click in search fashion items")

        #hover on fashion icon
        a.move_to_element(self.driver.find_element(*WishList.fashion_icon)).perform()
        #click on fashion dropdown
        self.driver.find_element(*WishList.fashion_dropdown).click()

        try:

            element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(WishList.fashion_dropdown))
            element.click()
            WishList.log.info("successfully visited to men's tshirt page")
        except (StaleElementReferenceException, TimeoutException, ElementClickInterceptedException):
            print("Failed to click in search fashion items")

    def add_items_to_wishlist(self):
        #declaring global variables to store items name
        global name_item_1, name_item_2
        try:
            #select fashion item 1
            element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(WishList.fashion_item_1))
            element.click()

            element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(WishList.fashion_item_1_name))

            name_item_1 = element.text
            # select fashion item 2
            element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(WishList.fashion_item_2))
            element.click()

            element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(WishList.fashion_item_2_name))
            name_item_2 = element.text
            print("item name 1: ", name_item_1)
            print("item name 2 ", name_item_2)

            WishList.log.info("successfully added items to list")
        except (StaleElementReferenceException, TimeoutException, ElementClickInterceptedException):
            print("Failed to click in add items to wishlist")





    #module for verifying items in wishlist
    def verify_items_in_wishlist(self):

        #creating object of actions class
        a = ActionChains(self.driver)
        a.move_to_element(self.driver.find_element(*WishList.my_account)).perform()
        try:
            #click on wishlist
            element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(WishList.wishlist))
            element.click()

            #storing name of item 1 from wishlist
            element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(WishList.wishlist_item_1_name))

            item_name_1_wishlist = element.text

            # storing name of item 1 from wishlist
            element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(WishList.wishlist_item_2_name))

            item_name_2_wishlist = element.text

            print("item name 1 wishlist : ", item_name_1_wishlist)
            print("item name 2 wishlist ", item_name_2_wishlist)

            # checking assertion condition for item 1 and wishlist item1
            self.assertIn(name_item_1, item_name_1_wishlist)
            # checking assertion condition for item 2 and wishlist item2
            self.assertIn(name_item_2, item_name_2_wishlist)

            if name_item_1 in item_name_1_wishlist and name_item_2 in item_name_2_wishlist:
                print("items verified in wishlist")

            WishList.log.info("successfully verified items in wishlist")
        except (StaleElementReferenceException, TimeoutException, ElementClickInterceptedException):
            print("Failed to click in verify items in wishlist")





