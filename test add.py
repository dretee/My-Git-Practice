# Import necessary modules and classes
import time
import requests
from Utilities import ReadXyfile
from selenium.webdriver.common.by import By
from Utilities.RecordLogger import RecordLogger
from Utilities.ReadProperties import ReadProperties
from PageObject.LoginObjects import LoginObjects

# to run the test use:   pytest -v -s TestCases/invalidLoginTestCase.py--browser chrome to run and also generate
# the html report use: pytest -v -s --html=Reports\reports.html TestCases/validLoginTestCase.py --browser chrome
"""
Negative test cases for the login page

Verify that a user cannot log in with an incorrect password.
Verify that a user cannot log in with an email that does not exist in the system.
Verify that a user cannot log in with an empty password field and email field.
Verify that a user cannot log in with an email containing special characters.
Verify the system's behavior after multiple failed login attempts.

"""


class Test_Login:
    # Initialize class variables with URLs, logger instance, and Excel file path
    URL = ReadProperties.getTestPageURL()  # Get main page URL from configuration
    ProductionURL = ReadProperties.getProductionPageURL()
    # loginPageUrl = ReadProperties.LoginURL()  # Get login page URL from configuration
    User_email, UserPassword = ReadProperties.getUserDetails()
    EXISTING_EMAIL = User_email  # Get existing email from configuration
    EXISTING_PASSWORD = UserPassword  # Get existing password
    # from configuration
    logger = RecordLogger.log_generator_info()  # Initialize logger instance
    PATH = ".\\TestData\\vnitpay data.xlsx"  # Excel file path

    # Method to log the start of a test
    def log_test_start(self, test_name):
        self.logger.info(f"****** STARTING TEST: {test_name} ******")

    # Method to log the end of a test
    def log_test_end(self, test_name):
        self.logger.info(f"****** ENDING TEST: {test_name} ******")

    # Method to open the website
    def open_website(self, setup, url):
        self.log_test_start("Open Website")
        self.driver = setup
        self.driver.get(url)
        self.driver.maximize_window()
        self.log_test_end("Open Website")
def test_the_login_of_users_with_wrong_password(self, setup):
    try:
        self.log_test_start("***** Verify that a user cannot log in with an incorrect password *****")
        self.open_website(setup, self.URL)
        self.LO = LoginObjects(self.driver)
        self.LO.input_email(self.EXISTING_EMAIL)
        self.LO.input_password("1232123")
        self.LO.click_on_the_signin_button()
        time.sleep(3)

        error_message = "Invalid username or password"
        assert error_message in self.driver.find_element(By.TAG_NAME, "body").text, self.logger.info(
            "*** TEST FAILED: THE USER WAS LOGGED INTO THE ACCOUNT ****")

        self.logger.info("**** TEST PASSED: THE USER WAS NOT LOGGED INTO THE ACCOUNT  *****")

    except AssertionError:
        self.logger.error("Assertion Error: Test condition failed.")
        raise  # Re-raise the exception to indicate test failure

    except Exception as e:
        self.logger.error(f"An unexpected error occurred: {e}")
        raise  # Re-raise the exception to indicate test failure

    finally:
        self.log_test_end("******* Verify that a user cannot log in with an incorrect password *******")
        self.driver.quit()


    finally:
        self.log_test_end("******* Verify that a user cannot log in with an incorrect password *******")
        self.driver.quit()

finally:
self.log_test_end("******* Verify that a user cannot log in with an incorrect password *******")
self.driver.quit()