import pytest
import allure
from selenium import webdriver
from ShopPage import ShopPage


first_name = "Natalia"
last_name = "Vasileva"
postal_code = "662311"
expected_total = "Total: $58.29"


@pytest.fixture
@allure.title("Подготовка драйвера браузера")
def driver():
    driver = webdriver.Edge()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Сравнение итоговой суммы заказа с ожидаемой стоимостью")
@allure.feature("Оформление заказа")
@allure.severity("CRITICAL")
@allure.description("""
Этот тест проверяет полный процесс оформления заказа в интернет-магазине:
1. Авторизация стандартного пользователя
2. Добавление товаров в корзину
3. Оформление заказа с вводом персональных данных
4. Проверка корректности итоговой суммы

Ожидаемый результат: Итоговая сумма должна быть равна $58.29
""")
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
    shop_page.input_your_data(first_name, last_name, postal_code)
    shop_page.waiting_loading_checkout_overview_page()

    with allure.step(
            "Проверка соответствия итоговой суммы заказа и ожидаемой"):
        actual_total = shop_page.get_total()
        assert actual_total == expected_total
