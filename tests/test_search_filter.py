import time
from selenium_mainassignment.pageobjects.search_filter import SearchFilter
from selenium_mainassignment.utilities.BaseClass import BaseClass
from selenium_mainassignment.testdata.Excel_operations import Excel_operation


#class TestSearchFilter
class TestSearchFilter(BaseClass):

    def test_search_filter(self):
        #creating object for logging
        log = self.getlogger()

        #sheetname where data is stored
        sheet_name = "Testcase3"

        #creating object for excel opeartions class
        excel_operation = Excel_operation()

        #storing data from excel to local variables
        search_item_name = excel_operation.read_data(sheet_name, 2, 1)
        filter_item_name = excel_operation.read_data(sheet_name, 2, 2)

        #creating object for SearchFitler class
        search_filter = SearchFilter(self.driver)
        time.sleep(10)
        #executing search item function
        search_filter.search_item(search_item_name)
        # executing filter item function
        search_filter.filter_item(filter_item_name)





