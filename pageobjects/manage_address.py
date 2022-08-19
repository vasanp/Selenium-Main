import time

from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_mainassignment.utilities.BaseClass import BaseClass


# class manageaddress
class ManageAddress():
    def __init__(self, driver):
        self.driver = driver

    # creating object for baseclass for accessing logging functions
    obj = BaseClass()
    log = obj.getlogger()

    # locators
    my_account = (By.XPATH, "/html/body/div/div//div[@class='_28p97w']/div")
    my_profile = (By.XPATH,
                  "/html/body//div[@class='ZEl_b_ _1J9ow0 _2ogGYG _23xUYh _3pAV4E']//div[@class='_3_Fivj']/div[@class='_1bQ5Pp']/ul[@class='pO9syL undefined']/li[1]")
    homepage = (By.XPATH, "/html/body//img[@title='Flipkart']")
    manage_address = (By.XPATH,
                      "/html/body//div[@class='_3SyQ96']//div[@class='_3E8aIl _3AJE9A']/div[2]//div[text()[contains(.,'Manage Addresses')]]")
    add_new_address = (By.XPATH, "/html/body//div[@class='w0WEfC']//div[@class='_1QhEVk']")
    name = (By.XPATH,
            "/html/body//div[@class='N5Ijry']/div[@class='_1hGj33']/div[@class='_1lRtwc _1Jqgld'][1]/input[@name='name']")
    phone = (By.XPATH,
             "/html/body//div[@class='N5Ijry']/div[@class='_1hGj33']/div[@class='_1lRtwc _1Jqgld'][2]/input[@name='phone']")
    pincode = (
        By.XPATH, "/html/body//div[@class='N5Ijry']/div[@class='_1hGj33'][2]/div[@class='_1lRtwc _1Jqgld'][1]/input")
    locality = (
        By.XPATH, "/html/body//div[@class='N5Ijry']/div[@class='_1hGj33'][2]/div[@class='_1lRtwc _1Jqgld'][2]/input")
    address = (By.XPATH,
               "/html/body//div[@class='N5Ijry']/div[@class='_1hGj33 _3kco7L']//div[@class='_1Y2dIb _1Jqgld']/textarea[@name='addressLine1']")
    address_type = (By.XPATH, "//div[@class='yI40P1']//label[1]")
    save_button = (By.XPATH, "/html/body//div[@class='N5Ijry']/div[@class='l5QiYB _1hGj33']/button")

    # code for visiting manage address page
    def visit_manage_address(self):
        # hover to my account tab
        a = ActionChains(self.driver)
        a.move_to_element(self.driver.find_element(*ManageAddress.my_account)).perform()

        try:
            # click on my profile
            element = WebDriverWait(self.driver, 25).until(
                EC.presence_of_element_located(ManageAddress.my_profile))
            element.click()
            ManageAddress.log.info("successfully visited managed address")

        except (StaleElementReferenceException, TimeoutException):
            print("Failed to click in visit manage address")

    # module for adding a new address
    def add_a_new_address(self, fields):
        a = ActionChains(self.driver)
        a.move_to_element(self.driver.find_element(*ManageAddress.my_account)).perform()
        try:
            # click on manage address
            element = WebDriverWait(self.driver, 25).until(
                EC.presence_of_element_located(ManageAddress.manage_address))
            element.click()
            # click on add new address
            element = WebDriverWait(self.driver, 25).until(
                EC.presence_of_element_located(ManageAddress.add_new_address))
            element.click()

            # enter name
            element = WebDriverWait(self.driver, 25).until(
                EC.presence_of_element_located(ManageAddress.name))
            element.send_keys(fields[0])

            # enter phone
            element = WebDriverWait(self.driver, 25).until(
                EC.presence_of_element_located(ManageAddress.phone))
            element.send_keys(fields[1])

            # enter pincode
            element = WebDriverWait(self.driver, 25).until(
                EC.presence_of_element_located(ManageAddress.pincode))
            element.send_keys(fields[2])

            # enter locality
            element = WebDriverWait(self.driver, 25).until(
                EC.presence_of_element_located(ManageAddress.locality))
            element.send_keys(fields[3])

            # enter address
            element = WebDriverWait(self.driver, 25).until(
                EC.presence_of_element_located(ManageAddress.address))
            element.send_keys(fields[4])

            # enter address type
            element = WebDriverWait(self.driver, 25).until(
                EC.presence_of_element_located(ManageAddress.address_type))
            element.click()

            ManageAddress.log.info("successfully visited managed address")

        except (StaleElementReferenceException, TimeoutException):
            print("Failed to click in add new address")

        try:
            # click on save button to save the new address
            element = WebDriverWait(self.driver, 25).until(
                EC.presence_of_element_located(ManageAddress.save_button))
            element.click()

            ManageAddress.log.info("successfully visited managed address")

            self.driver.quit()

        except (StaleElementReferenceException, TimeoutException):
            print("Failed to click in add new address")
