from locators.CustomerLoginPage import CustomerLogin
from locators.HomePage import HomePage
from locators.JacketsPage import Jackets
from locators.LandoJacketPage import LandoJacket
from utilities.BaseClass import BaseClass


class TestProductCart(BaseClass):

    def test_add_and_remove(self):
        self.log = self.getLogger()
        self.log.info("Test starting: Adding product to the cart.")
        self.driver.implicitly_wait(20)

        homePage = HomePage(self.driver)
        sign_in_customer = CustomerLogin(self.driver)
        homePage.sign_in()

        sign_in_customer.sign_in_action(TestCartData.email, TestCartData.password)
        homePage.click_on_man_jackets()

        jacketPage = Jackets(self.driver)
        assert "Jackets" in jacketPage.title_page()

        jacketPage.find_and_click_jacket(TestCartData.jacketName)

        landoJacket = LandoJacket(self.driver)
        assert TestCartData.jacketName in landoJacket.page_title()
        assert TestCartData.jacket_price in landoJacket.check_price()
        landoJacket.jacket_size()
        landoJacket.jacket_color()

        landoJacket.add_and_remove_from_cart_action()

        self.log.info("Test finished: Product added to the cart and removed from the cart.")























































