from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utilities.BaseClass import BaseClass


class MyAccount(BaseClass):

    registrationMessage = (By.CSS_SELECTOR, ".message-success")
    signOutButton = (By.XPATH, "//button[@class='action switch']")
    registrationFailureMessage = (By.XPATH, "//div[.='There is already an account with this email address. If you are sure that it is your email address, click here to get your password and access your account.']")

    def __init__(self, driver):
        self.driver = driver
        self.log = self.getLogger()

    def successful_registration(self):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(MyAccount.registrationMessage)
            )
            self.log.info("Successful registration message found.")
            return element.text
        except TimeoutException:
            self.log.error("Element not found or not visible within 20 seconds during successful registration.")
            raise

    def click_sign_out(self):
        try:
            sign_out_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MyAccount.signOutButton))
            sign_out_element.click()
            self.log.info("Clicked on Sign Out button.")
        except TimeoutException as e:
            self.log.error(f"Sign Out button not clickable within 10 seconds. Error: {e}")
        self.driver.find_element(By.LINK_TEXT, "Sign Out").click()

    def unsuccessful_registration(self):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(MyAccount.registrationFailureMessage)
            )
            self.log.info("Unsuccessful registration message found.")
            return element.text
        except TimeoutException:
            self.log.error("Element not found or not visible within 20 seconds during unsuccessful registration.")
            raise




