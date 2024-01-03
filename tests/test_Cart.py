from locators.CustomerLoginPage import CustomerLogin
from locators.HomePage import HomePage
from locators.JacketsPage import Jackets
from locators.LandoJacketPage import LandoJacket
from utilities.BaseClass import BaseClass


class TestProductCart(BaseClass):

    EMAIL = "vldmr@gmail.comm"
    PASSWORD = "Lalalala123123"
    JACKET_NAME = "Lando Gym Jacket"

    def test_add_and_remove(self):
        self.log = self.getLogger()
        self.log.info("Test starting: Adding product to the cart.")
        self.driver.implicitly_wait(20)

        homePage = HomePage(self.driver)
        sign_in_customer = CustomerLogin(self.driver)

        homePage.sign_in()
        sign_in_customer.email_log_in().send_keys(self.EMAIL)
        sign_in_customer.password_log_in().send_keys(self.PASSWORD)
        sign_in_customer.sing_in_button()

        homePage.click_on_man_jackets()
        jacketPage = Jackets(self.driver)

        assert "Jackets" in jacketPage.title_page()

        found_jacket = jacketPage.find_jacket(self.JACKET_NAME)
        if found_jacket:
            found_jacket.click()
            self.log.info(f"Product {self.JACKET_NAME} found and clicked.")
        else:
            self.log.warning(f"Product {self.JACKET_NAME} not found.")

        landoJakcet = LandoJacket(self.driver)
        assert self.JACKET_NAME in landoJakcet.page_title()
        assert "99.00" in landoJakcet.check_price()
        landoJakcet.jacket_size()
        landoJakcet.jacket_color()

        landoJakcet.add_to_cart_button()
        assert "You added Lando Gym Jacket to your shopping cart." in landoJakcet.confirm_message()
        landoJakcet.cart_button()
        landoJakcet.delete_button()
        landoJakcet.remove_button()
        try:
            assert "You have no items in your shopping cart." in landoJakcet.remove_message()
            self.log.info("Assertion: Successfully checked the shopping cart is empty.")
        except AssertionError as ae:
            self.log.error(f"Assertion failed: {ae}")
            raise

        self.log.info("Test finished: Product added to the cart and removed from the cart.")
























































