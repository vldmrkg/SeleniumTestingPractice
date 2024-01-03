from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from locators.CreateNewAccPage import CreateNewAccount
from utilities.BaseClass import BaseClass


class HomePage(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.log = self.getLogger()

    signIN = (By.LINK_TEXT, "Sign In")
    createAccount = (By.LINK_TEXT, "Create an Account")
    welcomeMessage = (By.XPATH, "//div[@class='panel header']//span[@class='logged-in'][normalize-space()='Welcome, Vladimir Timotijevic!']")
    searchBox = (By.XPATH, "//input[@name='q']")
    menProducts = (By.XPATH, "//span[normalize-space()='Men']")
    manTops = (By.XPATH, "//a[@id='ui-id-17']//span[contains(text(),'Tops')]")
    manJackets = (By.XPATH, "//a[@id='ui-id-19']")
    manHoodies = (By.LINK_TEXT, "Hoodies & Sweatshirts")
    products = (By.XPATH, "//div[@class='control']/div/ul/li")

    def sign_in(self):
        return self.driver.find_element(*HomePage.signIN).click()

    def create_account(self):
        self.driver.find_element(*HomePage.createAccount).click()
        newAccount = CreateNewAccount(self.driver)
        return newAccount

    def welcome_user_message(self):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(HomePage.welcomeMessage)
            )
            return element.text
        except TimeoutException:
            return "Element not found or not visible within 20 seconds."

    def search_box_input(self):
        return self.driver.find_element(*HomePage.searchBox)

    def hover_over_men_products(self):
        men_element = self.driver.find_element(*HomePage.menProducts)
        ActionChains(self.driver).move_to_element(men_element).perform()
        self.log.info("Hovered over Men products.")

    def hover_over_man_tops(self):
        self.hover_over_men_products()
        tops_element = self.driver.find_element(*HomePage.manTops)
        ActionChains(self.driver).move_to_element(tops_element).perform()
        self.log.info("Hovered over Men Tops.")

    def click_on_man_jackets(self):
        self.hover_over_man_tops()
        jackets_element = self.driver.find_element(*HomePage.manJackets)
        jackets_element.click()
        self.log.info("Clicked on Men Jackets.")

    def get_all_product_texts(self):
        product_elements = self.driver.find_elements(*HomePage.products)
        product_texts = [element.text for element in product_elements]
        return product_texts

    def perform_search_and_select_product(self, product_name):
        self.search_box_input().send_keys(product_name)
        self.log.info(f"Entered search term: '{product_name}' in the search box.")
        results = self.get_all_product_texts()

        for result in results:
            if "argus" in result.lower():
                product = WebDriverWait(self.driver, 20).until(
                    EC.visibility_of_element_located((By.ID, "qs-option-2"))
                )
                product.click()
                self.log.info(f"Selected product with search term: '{product_name}'.")
                break
            else:
                self.log.warning(f"No product found with search term: '{product_name}'.")
