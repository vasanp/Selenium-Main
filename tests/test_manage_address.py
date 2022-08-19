import time
from selenium_mainassignment.pageobjects.manage_address import ManageAddress
from selenium_mainassignment.utilities.BaseClass import BaseClass
from selenium_mainassignment.testdata.Excel_operations import Excel_operation


# class TestManageAddress
class TestManageAddress(BaseClass):

    def test_manage_address(self):
        # creating object for logger class
        log = self.getlogger()
        # sheet name where data is stored for testcase
        sheet_name = "Testcase5"

        # creating object for excel operation
        exceloperation = Excel_operation()

        # initializing empty list for retriving values from excel and storing
        fields = []

        # fetching values from excel and storing in list
        for i in range(1, 6):
            fields.append(exceloperation.read_data(sheet_name, 2, i))

        # creating object of manageaddress class
        manageaddress = ManageAddress(self.driver)
        time.sleep(10)

        # executing for visiting manage address page
        manageaddress.visit_manage_address()

        # executing function for adding new address
        manageaddress.add_a_new_address(fields)
