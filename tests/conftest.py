import pytest
from selenium import webdriver
import os


URL = ("https://magento.softwaretestingboard.com")


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):

    browser_name = request.config.getoption("browser_name")
    screenshot_dir = r"C:\Screenshots"

    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\\chromedriver.exe")

    elif browser_name == "opera":
        driver = webdriver.Opera(executable_path="C:\\Program Files (x86)\\operadriver.exe")

    elif browser_name == "edge":
        driver = webdriver.Edge(executable_path="C:\\Program Files (x86)\\msedgedriver.exe")

    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Program Files (x86)\\geckodriver.exe")

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.get(URL)
    driver.maximize_window()

    #provera da li je pocetna stranica ispravno ucitana

    expected_title = "Home Page"
    actual_title = driver.title

    assert actual_title == expected_title

    request.cls.driver = driver

    yield

    if request.session.testsfailed:
        test_name = request.node.name
        screenshot_path = os.path.join(screenshot_dir, f"{test_name}_failure.png")
        driver.save_screenshot(screenshot_path)
        print(f"\nScreenshot saved: {screenshot_path}")

    driver.close()

