from locators.CustomerLoginPage import CustomerLogin
from locators.MyAccountPage import MyAccount
from utilities.BaseClass import BaseClass
from locators.HomePage import HomePage


class TestSignIn(BaseClass):

    CORRECT_EMAIL = "vldmr@gmail.comm"
    CORRECT_PASSWORD = "Lalalala123123"
    INCORRECT_EMAIL = "vldmra@gmail.comm"
    INCORRECT_PASSWORD = "Lalalala123123sa"

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
        self.perform_sign_in(TestSignIn.CORRECT_EMAIL, TestSignIn.CORRECT_PASSWORD, "Welcome, Vladimir Timotijevic!")

    def test_sign_in_incorrect_data(self):
        self.perform_sign_in(TestSignIn.INCORRECT_EMAIL, TestSignIn.INCORRECT_PASSWORD)






















