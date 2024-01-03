from locators.CustomerLoginPage import CustomerLogin
from locators.MyAccountPage import MyAccount
from utilities.BaseClass import BaseClass
from locators.HomePage import HomePage


class TestSignIn(BaseClass):

    CORRECT_EMAIL = "vldmr@gmail.comm"
    CORRECT_PASSWORD = "Lalalala123123"
    INCORRECT_EMAIL = "vldmra@gmail.comm"
    INCORRECT_PASSWORD = "Lalalala123123sa"

    def test_sign_in_correct_data(self):
        log = self.getLogger()
        log.info("Testing sign-in with correct credentials begins.")

        homePage = HomePage(self.driver)
        homePage.sign_in()
        self.driver.implicitly_wait(15)

        logInPage = CustomerLogin(self.driver)
        assert logInPage.page_title() == "Customer Login"

        logInPage.email_log_in().send_keys(TestSignIn.CORRECT_EMAIL)
        logInPage.password_log_in().send_keys(TestSignIn.CORRECT_PASSWORD)
        logInPage.sing_in_button()
        assert homePage.welcome_user_message() == "Welcome, Vladimir Timotijevic!"
        logOut = MyAccount(self.driver)
        logOut.click_sign_out()
        log.info("Testing sign-in with correct credentials completed.")

    def test_sign_in_incorrect_data(self):
        log = self.getLogger()
        log.info("Testing sign-in with incorrect credentials begins.")

        homePage = HomePage(self.driver)
        homePage.sign_in()
        self.driver.implicitly_wait(15)

        logInPage = CustomerLogin(self.driver)
        assert logInPage.page_title() == "Customer Login"
        logInPage.email_log_in().send_keys(TestSignIn.INCORRECT_EMAIL)
        logInPage.password_log_in().send_keys(TestSignIn.INCORRECT_PASSWORD)
        logInPage.sing_in_button()
        assert "The account sign-in was incorrect" in logInPage.alert_message()

        log.info("Testing sign-in with incorrect credentials completed.")






















