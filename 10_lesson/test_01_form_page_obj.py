import pytest
from selenium import webdriver
from FormPage import FormPage
import allure


@pytest.fixture
@allure.title("Подготовка драйвера браузера")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка полного цикла отправки формы")
@allure.feature("Форма")
@allure.severity("BLOCKER")
@allure.description("""
Тест проверяет отправку формы с необходимыми данными:
1. Открытие страницы формы
2. Заполнение всех полей
3. Отправка формы
4. Проверка валидации полей

Ожидаемый результат:
- Поле zip-code показывает ошибку (пустое поле)
- Все остальные поля показывают успешную валидацию
""")
def test_form_submission_flow(driver):
    form_page = FormPage(driver)
    form_page.open()
    form_page.fill_form()
    form_page.submit_form()
    form_page.check_form_submission()
