from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass


class CheckOut(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.log = self.getLogger()

    email = (By.XPATH, "//div[@class='control _with-tooltip']//input[@id='customer-email']")
    firstName = (By.NAME, "firstname")
    lastName = (By.NAME, "lastname")
    company = (By.NAME, "company")
    street = (By.NAME, "street[0]")
    city = (By.NAME, "city")
    state = (By.NAME, "region_id")
    zip = (By.NAME, "postcode")
    country = (By.NAME, "country_id")
    phone = (By.NAME, "telephone")
    checkBox = (By.CSS_SELECTOR, "tbody tr:nth-child(2) td:nth-child(2) span:nth-child(1) span:nth-child(1)")
    nextButton= (By.CSS_SELECTOR, ".button.action.continue.primary")

    def email_field(self):

        email_element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckOut.email)
        )
        return email_element

    def first_name_field(self):
        return self.driver.find_element(*CheckOut.firstName)

    def last_name_field(self):
        return self.driver.find_element(*CheckOut.lastName)

    def company_name(self):
        return self.driver.find_element(*CheckOut.company)

    def sreet_address(self):
        return self.driver.find_element(*CheckOut.street)

    def city_name(self):
        return self.driver.find_element(*CheckOut.city)

    def select_state(self):
        wait = WebDriverWait(self.driver, 10)
        dropdown = wait.until(EC.visibility_of_element_located(CheckOut.state))
        select = Select(dropdown)
        select.select_by_value("57")

    def zip_code(self):
        return self.driver.find_element(*CheckOut.zip)

    def select_country(self):
        wait = WebDriverWait(self.driver, 10)
        dropdown = wait.until(EC.visibility_of_element_located(CheckOut.country))
        select = Select(dropdown)
        select.select_by_value("US")

    def phone_number(self):
        return self.driver.find_element(*CheckOut.phone)

    def check_box(self):
        return self.driver.find_element(*CheckOut.checkBox).click()

    def next_button(self):
        return self.driver.find_element(*CheckOut.nextButton).click()

    def fill_out_shipping_information(self, get_fake_data):
        self.log.info("Filling out shipping information.")
        self.email_field().send_keys(get_fake_data["email"])
        self.first_name_field().send_keys(get_fake_data["firstname"])
        self.last_name_field().send_keys(get_fake_data["lastname"])
        self.company_name().send_keys(get_fake_data["company"])
        self.sreet_address().send_keys(get_fake_data["street"])
        self.city_name().send_keys(get_fake_data["city"])
        self.select_state()
        self.zip_code().send_keys(get_fake_data["zipCode"])
        self.select_country()
        self.phone_number().send_keys(get_fake_data["phoneNumber"])
        self.check_box()
        self.log.info("Shipping information filled out successfully.")
        self.next_button()











