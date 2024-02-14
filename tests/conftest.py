import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
import os


URL = "https://magento.softwaretestingboard.com"


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name == "opera":
        driver = webdriver.Opera(OperaDriverManager().install())
    elif browser_name == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    elif browser_name == "firefox":
        driver = webdriver.Firefox(GeckoDriverManager().install())
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.get(URL)
    driver.maximize_window()

    # Provera da li je pocetna stranica ispravno ucitana
    expected_title = "Home Page"
    actual_title = driver.title
    assert actual_title == expected_title

    request.cls.driver = driver

    yield

    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Specify browser name: chrome, opera, edge, firefox"
    )
