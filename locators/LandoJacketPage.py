from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass


class LandoJacket(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.log = self.getLogger()

    titlePage = (By.XPATH, "//span[@itemprop='name']")
    price = (By.ID, "product-price-334")
    size = (By.XPATH, "//div[@id='option-label-size-143-item-169']")
    color = (By.XPATH, "//div[@id='option-label-color-93-item-50']")
    addToCart = (By.XPATH, "//span[normalize-space()='Add to Cart']")
    message = (By.CSS_SELECTOR, ".message-success")
    cart = (By.XPATH, "//a[@class='action showcart']")
    checkout = (By.XPATH, "//button[@id='top-cart-btn-checkout']")
    deleteButton = (By.XPATH, "//a[@title='Remove item']")
    popUpMsg = (By.CSS_SELECTOR, ".action-primary")
    removeMessage = (By.XPATH, "//strong[@class='subtitle empty']")

    def page_title(self):
        self.log.info("Retrieving page title.")
        return self.driver.find_element(*LandoJacket.titlePage).text

    def check_price(self):
        self.log.info("Checking the price of the jacket.")
        return self.driver.find_element(*LandoJacket.price).text

    def jacket_size(self):
        self.log.info("Selecting jacket size.")
        return self.driver.find_element(*LandoJacket.size).click()

    def jacket_color(self):
        self.log.info("Selecting jacket color.")
        return self.driver.find_element(*LandoJacket.color).click()

    def add_to_cart_button(self):
        self.log.info("Clicking on 'Add to Cart' button.")
        return self.driver.find_element(*LandoJacket.addToCart).click()

    def confirm_message(self):
        try:
            self.log.info("Verifying the success message after adding to cart.")
            return WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(LandoJacket.message)
            ).text
        except TimeoutException as e:
            self.log.error(f"Error verifying success message: {e}")
            return None

    def cart_button(self):
        try:
            self.log.info("Clicking on the 'Cart' button.")
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(LandoJacket.cart)
            ).click()
        except TimeoutException as e:
            self.log.error(f"Error clicking 'Cart' button: {e}")

    def check_out_button(self):
        try:
            self.log.info("Clicking on the 'Checkout' button.")
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(LandoJacket.checkout)
            ).click()
        except TimeoutException as e:
            self.log.error(f"Error clicking 'Checkout' button: {e}")

    def delete_button(self):
        try:
            self.log.info("Clicking on the 'Delete' button.")
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(LandoJacket.deleteButton)
            ).click()
        except TimeoutException as e:
            self.log.error(f"Error clicking 'Delete' button: {e}")

    def remove_button(self):
        try:
            self.log.info("Clicking on the 'Remove' button in the confirmation popup.")
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(LandoJacket.popUpMsg)
            ).click()
        except TimeoutException as e:
            self.log.error(f"Error clicking 'Remove' button: {e}")

    def remove_message(self):
        try:
            self.log.info("Verifying the message after removing the item.")
            return WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(LandoJacket.removeMessage)
            ).text
        except TimeoutException as e:
            self.log.error(f"Error verifying remove message: {e}")
            return None

    def add_and_remove_from_cart_action(self):
        self.add_to_cart_button()
        assert "You added Lando Gym Jacket to your shopping cart." in self.confirm_message()
        self.cart_button()
        self.delete_button()
        self.remove_button()

        try:
            assert "You have no items in your shopping cart." in self.remove_message()
            self.log.info("Assertion: Successfully checked the shopping cart is empty.")
        except AssertionError as ae:
            self.log.error(f"Assertion failed: {ae}")
            raise












