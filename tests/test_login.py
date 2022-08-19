from selenium_mainassignment.utilities.BaseClass import BaseClass


class TestLogin(BaseClass):



    def test_home(self):
       #Creating object of logger
       log = self.getlogger()

       log.info("Login and Logout working")

