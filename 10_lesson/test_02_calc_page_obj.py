import pytest
import allure
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from CalcMainPage import CalcMainPage


@pytest.fixture
@allure.title("Подготовка драйвера браузера")
def driver():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install())
    )
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.parametrize(
    "num1, operation, num2, expected_result, delay",
    [
        ("7", "+", "8", "15", 15),
        ("9", "-", "3", "6", 10),
        ("4", "x", "5", "20", 20),
        ("8", "÷", "2", "4", 5),
    ],
)
@allure.title("Проверка операций калькулятора: {num1} {operation} {num2} "
              "= {expected_result} с задержкой {delay} секунд")
@allure.feature("Калькулятор")
@allure.severity("CRITICAL")
@allure.description("""
Тест проверяет основные операции калькулятора,
при этом учитывает задержку вычислений
и ожидает правильный результат.
""")
def test_calculator_flow(driver, num1, operation,
                         num2, expected_result, delay):
    main_page = CalcMainPage(driver)

    main_page.open()
    main_page.set_delay(delay)
    main_page.click_buttons([num1, operation, num2, "="])
    main_page.wait_for_result(expected_result, delay)

    with allure.step("Проверяет, что результат на экране калькулятора "
                     "совпадает с ожидаемым результатом"):
        assert main_page.get_result() == expected_result, \
            (f"Expected result:{expected_result}, "
             f"but got:{main_page.get_result()}")
