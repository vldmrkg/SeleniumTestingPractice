from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    orderButton = (By.XPATH, "//span[normalize-space()='Place Order']")

    def place_order(self):
        place_order_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(ConfirmPage.orderButton),
            "Place order button not clickable within 20 seconds."
        )
        # JavaScript Executor perform click
        self.driver.execute_script("arguments[0].click();", place_order_button)
