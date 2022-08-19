import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium_mainassignment.pageobjects.login import Login
from selenium_mainassignment.testdata.Excel_operations import Excel_operation


@pytest.fixture(scope="class")
def setup(request):
    # opening the browser
    s: Service = Service(
        '/Users/vasanp/PycharmProjects/pythonProject/selenium_mainassignment/Resources'
        '/chromedriver')

    driver = webdriver.Chrome(service=s)

    # maximizing the window
    driver.maximize_window()

    # opening the url
    driver.get('https://www.flipkart.com/')

    #sheet name of credentials
    name_sheet = "users"
    #creating object of excel operations
    excel_operation = Excel_operation()
    #storing data to local variables
    username = excel_operation.read_data(name_sheet, 2, 1)
    password = excel_operation.read_data(name_sheet, 2, 2)

    login = Login(driver)
    login.login_process(username, password)

    request.cls.driver = driver
    yield
    # logging out and closing browser
    login.logout_process()







