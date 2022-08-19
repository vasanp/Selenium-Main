import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
#class login
from selenium_mainassignment.utilities.BaseClass import BaseClass


class Login:
    def __init__(self, driver):
        self.driver = driver

    #creating object for logging
    obj = BaseClass()
    #log = obj.getlogger()

    #locators
    email = (By.XPATH, "/html/body//div[@class='_2Sn47c']//form//input[@class='_2IX_2- VJZDxU']")
    password = (By.XPATH, "/html/body//div[@class='_2Sn47c']//form//input[@class='_2IX_2- _3mctLh VJZDxU']")
    login_button = (By.XPATH, "/html/body//div[@class='_2Sn47c']//form//button[@class='_2KpZ6l _2HKlqd _3AWRsL']")
    my_account = (By.XPATH, "/html/body/div/div//div[@class='_28p97w']/div")
    logout_button = (By.XPATH,
                     "/html/body//div[@class='ZEl_b_ _1J9ow0 _2ogGYG _23xUYh _3pAV4E']//div[@class='_3_Fivj']/div[@class='_1bQ5Pp']/ul/li/a[@href='#']")

    #module for login
    def login_process(self, username, password):
        #entering username and password
        self.driver.find_element(*Login.email).send_keys(username)
        self.driver.find_element(*Login.password).send_keys(password)
        #click login to enter the portal
        self.driver.find_element(*Login.login_button).click()

    #module for logout
    def logout_process(self):
        #creating object of actions class
        a = ActionChains(self.driver)
        time.sleep(5)
        #hovering on my account
        a.move_to_element(self.driver.find_element(*Login.my_account)).perform()
        time.sleep(5)

        #click on logout button
        self.driver.find_element(*Login.logout_button).click()
       # Login.log.info("Successfully Logged out")
        time.sleep(3)
        self.driver.quit()
