from locators.CustomerLoginPage import CustomerLogin
from testData.fakeData import SignInPageData
from utilities.BaseClass import BaseClass
from locators.HomePage import HomePage


class TestSignIn(BaseClass):

    def test_sign_in_correct_data(self):
        home_page = HomePage(self.driver)
        log_in_page = CustomerLogin(self.driver)

        correct_email, correct_password = SignInPageData.get_correct_signin_data()
        log_in_page.perform_sign_in(correct_email, correct_password, home_page, "Welcome, Vladimir Timotijevic!")

    def test_sign_in_incorrect_data(self):
        home_page = HomePage(self.driver)
        log_in_page = CustomerLogin(self.driver)

        incorrect_email, incorrect_password = SignInPageData.get_incorrect_signin_data()
        log_in_page.perform_sign_in(incorrect_email, incorrect_password, home_page)





















