import time
import pytest
from locators.CreateNewAccPage import CreateNewAccount
from locators.HomePage import HomePage
from locators.MyAccountPage import MyAccount
from testData.fakeData import HomePageData
from utilities.BaseClass import BaseClass


class TestRegistration(BaseClass):

    def test_register_user(self, getData):
        log = self.getLogger()
        log.info("User registration testing begins.")

        homePage = HomePage(self.driver)
        myAccount = MyAccount(self.driver)
        newAccount = CreateNewAccount(self.driver)
        new_account_page = newAccount.create_new_account(homePage)
        assert new_account_page is not None, "Failed to create a new account page."
        newAccount.fill_out_registration_form(new_account_page, getData)
        assert myAccount.successful_registration() == "Thank you for registering with Main Website Store."
        myAccount.click_sign_out()
        time.sleep(6)

        log.info("User registration testing completed.")

    def test_register_user_existing_email(self):
        log = self.getLogger()
        log.info("User registration testing with existing email begins.")

        try:
            EXISTING_EMAIL = "vldmr@gmail.comm"
            homePage = HomePage(self.driver)
            newAccount = homePage.create_account()

            newAccount.first_name().send_keys("Mario")
            newAccount.last_name().send_keys("Markis")
            newAccount.email_input().send_keys(EXISTING_EMAIL)
            newAccount.password_input().send_keys("Sifra123")
            newAccount.password_confirm().send_keys("Sifra123")
            newAccount.create_account().click()

            registration_confirmation = MyAccount(self.driver)
            assert "There is already an account with this email address." in registration_confirmation.unsuccessful_registration()

            log.info("User registration testing with existing email completed.")

        except Exception as e:
            log.error(f"Error during user registration with existing email: {str(e)}")

    @pytest.fixture(params=HomePageData.test_homePage_data)
    def getData(self, request):
        return request.param






















