from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.BaseClass import BaseClass


class SuccessPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.log = self.getLogger()

    message_locator = (By.XPATH, "//*[@id='maincontent']/div[1]/h1/span")

    def success_message(self):
        try:
            self.log.info("Waiting for the success message to be present.")
            WebDriverWait(self.driver, 20).until(
                EC.text_to_be_present_in_element(SuccessPage.message_locator, "Thank you for your purchase!")
            )
            message_element = self.driver.find_element(*SuccessPage.message_locator)
            success_message = message_element.text
            self.log.info(f"Success message found: {success_message}")
            return success_message
        except TimeoutException:
            error_message = "Element not found or not visible within 20 seconds."
            self.log.error(error_message)

            return error_message