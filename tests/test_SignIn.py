from locators.CustomerLoginPage import CustomerLogin
from locators.MyAccountPage import MyAccount
from utilities.BaseClass import BaseClass
from locators.HomePage import HomePage


class TestSignIn(BaseClass):

    def perform_sign_in(self, email, password, expected_welcome_message=None):
        log = self.getLogger()
        log.info(f"Testing sign-in with {'correct' if expected_welcome_message else 'incorrect'} credentials begins.")

        homePage = HomePage(self.driver)
        homePage.sign_in()
        self.driver.implicitly_wait(15)

        logInPage = CustomerLogin(self.driver)
        assert logInPage.page_title() == "Customer Login"

        logInPage.enter_email(email)
        logInPage.enter_password(password)
        logInPage.sign_in_button()

        if expected_welcome_message:
            assert homePage.welcome_user_message() == expected_welcome_message
            logOut = MyAccount(self.driver)
            logOut.click_sign_out()
            log.info("Testing sign-in with correct credentials completed.")
        else:
            assert "The account sign-in was incorrect" in logInPage.alert_message()
            log.info("Testing sign-in with incorrect credentials completed.")

    def test_sign_in_correct_data(self):
        correct_email, correct_password = SignInPageData.get_correct_signin_data()
        self.perform_sign_in(correct_email, correct_password, "Welcome, Vladimir Timotijevic!")

    def test_sign_in_incorrect_data(self):
        incorrect_email, incorrect_password = SignInPageData.get_incorrect_signin_data()
        self.perform_sign_in(incorrect_email, incorrect_password)





















