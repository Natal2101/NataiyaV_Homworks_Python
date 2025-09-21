import pytest
from selenium import webdriver

from pages.ShopPage import ShopPage


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_comparing_receipt_goods_total(driver):
    shop_page = ShopPage(driver)
    shop_page.open()
    shop_page.waiting_loading_main_page()
    shop_page.authorization_standard_user()
    shop_page.waiting_loading_products_page()
    shop_page.add_item_to_cart()
    shop_page.waiting_loading_your_cart_page()
    shop_page.button_checkout_click()
    shop_page.waiting_loading_your_information_page()
    shop_page.input_your_data()
    shop_page.waiting_loading_checkout_overview_page()

    total = shop_page.get_total()
    assert total == "Total: $58.29"
