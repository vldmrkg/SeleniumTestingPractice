import time
import pytest
from selenium.common.exceptions import TimeoutException
from locators.CheckOutPage import CheckOut
from locators.ConfirmPage import ConfirmPage
from locators.HomePage import HomePage
from locators.SearchResultsPage import SearchResults
from locators.SuccessPage import SuccessPage
from testData.fakeData import CheckOutPageData
from utilities.BaseClass import BaseClass


class TestEnd2End(BaseClass):

    def test_e2e(self, get_fake_data):
        self.driver.implicitly_wait(30)
        log = self.getLogger()

        homePage = HomePage(self.driver)
        log.info("End-to-end test begins")
        time.sleep(1)

        log.info("Performing search and selecting a product")

        homePage.perform_search_and_select_product("arg")
        searchPage = SearchResults(self.driver)

        log.info("Performing actions on the search results page")

        searchPage.perform_actions()
        checkOutPage = CheckOut(self.driver)

        log.info("Filling in delivery information")

        try:
            checkOutPage.fill_out_shipping_information(get_fake_data)
        except TimeoutException:
            log.error("TimeoutException occurred while filling out shipping information.")

        confirmPage = ConfirmPage(self.driver)

        log.info("Placing the order")

        confirmPage.place_order()
        success_page = SuccessPage(self.driver)
        textMsg = success_page.success_message()
        assert "Thank you for your purchase!" == textMsg
        log.info("Success message verified.")

        log.info("End-to-end test completed")

    @pytest.fixture(params=CheckOutPageData.test_checkOutPage_data)
    def get_fake_data(self, request):
        return request.param








