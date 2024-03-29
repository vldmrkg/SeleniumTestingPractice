from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CustomerLogin(BaseClass):

    def __init__(self, driver):
        self.driver = driver

        self.titlePage = (By.XPATH, "//span[@class='base']")
        self.logInEmail = (By.XPATH, "//input[@name='login[username]']")
        self.logInPasswrod = (By.XPATH, "//input[@name='login[password]']")
        self.signInButton = (By.XPATH, "//button[@id='send2'][.='Sign In']")
        self.allertMessage = (By.CSS_SELECTOR, ".message-error.error.message")

    def page_title(self):
        return self.driver.find_element(*self.titlePage).text

    def enter_email(self, email):
        return self.driver.find_element(*self.logInEmail).send_keys(email)

    def enter_password(self, password):
        return self.driver.find_element(*self.logInPasswrod).send_keys(password)

    def sign_in_button(self):
        return self.driver.find_element(*self.signInButton).click()

    def alert_message(self):
        try:
            message = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(self.allertMessage)
            )
            return message.text
        except TimeoutException:
            return "Element not found or not visible within 10 seconds."

    def perform_sign_in(self, email, password, home_page, expected_welcome_message=None):
        log = BaseClass.getLogger()

        if expected_welcome_message:
            log.info("Testing sign-in with correct credentials begins.")
        else:
            log.info("Testing sign-in with incorrect credentials begins.")

        home_page.sign_in()
        self.driver.implicitly_wait(15)

        assert self.page_title() == "Customer Login"

        self.enter_email(email)
        self.enter_password(password)
        self.sign_in_button()

        if expected_welcome_message:
            self.verify_successful_sign_in(home_page, expected_welcome_message)
        else:
            self.verify_unsuccessful_sign_in()

    def verify_successful_sign_in(self, home_page, expected_welcome_message):
        log = BaseClass.getLogger()

        welcome_message = home_page.welcome_user_message()
        assert welcome_message == expected_welcome_message
        log.info(f"Successful sign-in. Welcome message: {welcome_message}")

        self.perform_sign_out(log, home_page)
        log.info("Testing sign-in with correct credentials completed.")

    def verify_unsuccessful_sign_in(self):
        log = BaseClass.getLogger()

        alert_msg = self.alert_message()
        assert "The account sign-in was incorrect" in alert_msg
        log.info(f"Unsuccessful sign-in. Alert message: {alert_msg}")
        log.info("Testing sign-in with incorrect credentials completed.")

    def perform_sign_out(self, log, home_page):
        logOut = MyAccount(self.driver)
        logOut.click_sign_out()
        log.info("User signed out successfully.")

    def sign_in_action(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.sign_in_button()










