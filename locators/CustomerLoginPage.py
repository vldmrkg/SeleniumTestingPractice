from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CustomerLogin:

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














