from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.BaseClass import BaseClass


class Jackets(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.log = self.getLogger()

    pageTitle = (By. XPATH, "//span[@class='base']")
    jacketTitles = (By.CSS_SELECTOR, ".products-grid ol li")

    def title_page(self):
        title = self.driver.find_element(*Jackets.pageTitle).text
        self.log.info(f"Page title: {title}")
        return title

    def find_jacket(self, jacketName):
        try:
            products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(self.jacketTitles)
            )

            for product in products:
                try:
                    jacket = WebDriverWait(product, 10).until(
                        EC.presence_of_element_located((By.XPATH, f"//a[normalize-space()='{jacketName}']"))
                    )
                    self.log.info(f"Found jacket with name: '{jacketName}'")
                    return jacket
                except TimeoutException:
                    self.log.warning(f"Element with name '{jacketName}' not found in product.")
        except TimeoutException:
            self.log.warning("Products list not found or empty.")
        return None





