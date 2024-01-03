from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class CreateNewAccount(BaseClass):

    def __init__(self, driver):
        self.driver = driver
        self.log = self.getLogger()

    firstName = (By.XPATH, "//input[@id='firstname']")
    lastName = (By.XPATH, "//input[@id='lastname']")
    emailField = (By.XPATH, "//input[@id='email_address']")
    password = (By.XPATH, "//input[@id='password']")
    passConfirm = (By.XPATH, "//input[@id='password-confirmation']")
    createAcc = (By.XPATH, "//button[@title='Create an Account']//span[contains(text(),'Create an Account')]")

    def first_name(self):
        return self.driver.find_element(*CreateNewAccount.firstName)

    def last_name(self):
        return self.driver.find_element(*CreateNewAccount.lastName)

    def email_input(self):
        return self.driver.find_element(*CreateNewAccount.emailField)

    def password_input(self):
        return self.driver.find_element(*CreateNewAccount.password)

    def password_confirm(self):
        return self.driver.find_element(*CreateNewAccount.passConfirm)

    def create_account(self):
        return self.driver.find_element(*CreateNewAccount.createAcc)

    def create_new_account(self, home_page):
        new_account = home_page.create_account()
        return new_account

    def fill_out_registration_form(self, new_account_page, data):
        self.log.info("Filling out registration form.")
        new_account_page.first_name().send_keys(data["firstname"])
        new_account_page.last_name().send_keys(data["lastname"])
        new_account_page.email_input().send_keys(data["email"])
        new_account_page.password_input().send_keys(data["password"])
        new_account_page.password_confirm().send_keys(data["password"])
        new_account_page.create_account().click()
        self.log.info("Registration form filled out successfully.")







