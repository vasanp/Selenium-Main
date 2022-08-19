import unittest
from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_mainassignment.utilities.BaseClass import BaseClass


class SearchFilter(unittest.TestCase):
    def __init__(self, driver):
        self.driver = driver

    #creating object for baseclass to access logging functions
    obj = BaseClass()
    log = obj.getlogger()
    variable = "Tata"
    search_box = (By.XPATH, "/html/body//form//input")
    search_submit = (By.XPATH, "/html/body//form//button[@type='submit']")
    search_brand = (By.XPATH, "//input[@placeholder='Search Brand']")
    checkbox = "//div[@title='{}']".format(variable)
    filter_checkbox = (By.XPATH, checkbox)
    filter_title = (By.XPATH, "/html/body//div[@class='_36fx1h _6t1WkM _3HqJxg']//label[@class='_2iDkf8 t0pPfW']/div[2]")
    filtered_item = (By.XPATH, "/html/body/div//div[@class='_1AtVbE col-12-12']/div[@class='_13oc-S']/div[1]//a[@title='Tata Besan 100% Chana Dal, 1 kg']")

    #module for searching item
    def search_item(self, search_item_name):
        try:
            # wait 10 seconds before looking for element
            #search item on search box
            element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(SearchFilter.search_box))
            element.send_keys(search_item_name)

            #click submit button to search the item
            element2 = WebDriverWait(self.driver, 25).until(
                EC.presence_of_element_located(SearchFilter.search_submit))
            element2.click()

            SearchFilter.log.info("searched item successfully")
        except (StaleElementReferenceException, TimeoutException):
            print("Failed to click in search item")

    #module for filtering item
    def filter_item(self, filter_checkbox_name):
        try:
            # wait 10 seconds before looking for element
            #search brand in filter
            element = WebDriverWait(self.driver, 25).until(
                EC.presence_of_element_located(SearchFilter.search_brand))
            element.send_keys(filter_checkbox_name)

            #click on checkbox
            element = WebDriverWait(self.driver, 25).until(
                EC.presence_of_element_located(SearchFilter.filter_checkbox))
            element.click()

            #get title of item
            element = WebDriverWait(self.driver, 25).until(
                EC.presence_of_element_located(SearchFilter.filter_title))
            filter_name = element.text

            print("filter name: ", filter_name)

            #storing name of result item after filtering
            element = WebDriverWait(self.driver, 25).until(
                EC.presence_of_element_located(SearchFilter.filtered_item))
            filtered_item_name = element.text

            print("filtered item name: ", filtered_item_name)

            #checking assertion condition for filter name and filtered item name
            self.assertIn(filter_name, filtered_item_name)

            #if condition for checking the same
            if filter_name in filtered_item_name:
                print("item filtered ")

            SearchFilter.log.info("filtered item successfully")
        except (StaleElementReferenceException, TimeoutException):
            print("Failed to click in filter item")


