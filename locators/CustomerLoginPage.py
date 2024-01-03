from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CustomerLogin:

    def __init__(self, driver):
        self.driver = driver
    titlePage = (By.XPATH, "//span[@class='base']")
    logInEmail = (By.XPATH, "//input[@name='login[username]']")
    logInPasswrod = (By.XPATH, "//input[@name='login[password]']")
    signInButton = (By.XPATH, "//button[@id='send2'][.='Sign In']")
    allertMessage = (By.CSS_SELECTOR, ".message-error.error.message")

    def page_title(self):
        return self.driver.find_element(*CustomerLogin.titlePage).text

    def email_log_in(self):
        return self.driver.find_element(*CustomerLogin.logInEmail)

    def password_log_in(self):
        return self.driver.find_element(*CustomerLogin.logInPasswrod)

    def sing_in_button(self):
        return self.driver.find_element(*CustomerLogin.signInButton).click()

    def alert_message(self):
        try:
            message = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(CustomerLogin.allertMessage)
            )
            return message.text
        except TimeoutException:
            return "Element not found or not visible within 10 seconds."














