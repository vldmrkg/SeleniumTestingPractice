import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass


class SearchResults(BaseClass):

    def __init__(self, driver):
        self.driver = driver
        self.log = self.getLogger()

    size = (By.XPATH, "//div[@id='option-label-size-143-item-166']")
    color = (By.XPATH, "//div[@id='option-label-color-93-item-52']")
    addButton = (By.XPATH, "//span[normalize-space()='Add to Cart']")
    cartButton = (By.XPATH, "//span[@class='counter-number']")
    checkOut = (By.ID, "top-cart-btn-checkout")

    def click_size(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(SearchResults.size),
                "Size button not clickable within 20 seconds."
            ).click()
            self.log.info("Clicked on size button.")
        except Exception as e:
            self.log.error(f"Error clicking size button: {e}")

    def click_color(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(SearchResults.color),
                "Color button not clickable within 20 seconds."
            ).click()
            self.log.info("Clicked on color button.")
        except Exception as e:
            self.log.error(f"Error clicking color button: {e}")

    def click_add(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(SearchResults.addButton),
                "Add button not clickable within 20 seconds."
            ).click()
            self.log.info("Clicked on add button.")
        except Exception as e:
            self.log.error(f"Error clicking add button: {e}")

    def click_cart(self):
        try:
            element = self.driver.find_element(*SearchResults.cartButton)
            # Skrolovanje do određenog elementa pomoću JavaScript-a
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            WebDriverWait(self.driver, 20).until(lambda driver: driver.execute_script('return jQuery.active == 0'))   # Asinhroni zahtevi da se završe
            element.click()
            self.log.info("Clicked on cart button.")
            time.sleep(1)
        except Exception as e:
            self.log.error(f"Error clicking cart button: {e}")

    def check_out_button(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(SearchResults.checkOut),
                "Checkout button not visible within 30 seconds."
            ).click()
            self.log.info("Clicked on checkout button.")
        except Exception as e:
            self.log.error(f"Error clicking checkout button: {e}")

    def perform_actions(self):
        self.click_size()
        self.click_color()
        self.click_add()
        self.click_cart()
        self.check_out_button()


