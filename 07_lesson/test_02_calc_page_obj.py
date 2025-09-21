import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from pages.CalcPage import CalcPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install())
    )
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_waiting_get_result(driver):
    calc_page = CalcPage(driver)
    calc_page.open()
    calc_page.input_45()
    calc_page.input_numbers()
    calc_page.wait_45_seconds()
    result = calc_page.get_result()
    assert result == "15"
