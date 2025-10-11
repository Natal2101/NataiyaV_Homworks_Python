from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.epic("Форма отправки")
class FormPage:
    """
        Класс для работы с веб-страницей формы.
        Этот класс предоставляет методы для открытия страницы формы,
        управления элементами формы, такими как заполнение полей,
        отправка формы и проверка состояния полей.
    """

    @allure.step("Инициализирует экземпляр страницы. "
                 "Параметр driver: WebDriver")
    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.fields = {
            'first-name': "Иван",
            'last-name': "Петров",
            'address': "Ленина, 55-3",
            'zip-code': "",
            'city': "Москва",
            'country': "Россия",
            'e-mail': "test@skypro.com",
            'phone': "+7985899998787",
            'job-position': "QA",
            'company': "SkyPro"
        }

    @allure.step("Открывает страницу формы в браузере по указанному URL")
    def open(self) -> None:
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
            )

    @allure.step("Заполняет форму, используя значения из словаря fields")
    def fill_form(self) -> None:
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located((
                    By.NAME, field))).send_keys(value)

    @allure.step("Нажимает кнопку отправки формы")
    def submit_form(self) -> None:
        button = self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
        # self.wait.until(
        #     EC.element_to_be_clickable((
        #         By.CSS_SELECTOR, '[type="submit"]'))).click()
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        self.driver.execute_script("arguments[0].click();", button)

    @allure.step("Возвращает значение атрибута class поля, "
                 "заданного по ID {field_id}")
    def get_field_class(self, field_id: str) -> str:
        element = self.wait.until(
            EC.presence_of_element_located((
                By.ID, field_id))).get_attribute("class")
        return element

    @allure.step("Проверяет, есть ли ошибка в поле 'zip-code'")
    def check_zip_code_error(self) -> bool:
        return "alert-danger" in self.get_field_class("zip-code")

    @allure.step("Проверяет, прошли ли все поля успешно валидацию")
    def check_fields_success(self) -> bool:
        fields = ['first-name', 'last-name', 'address', 'e-mail', 'phone',
                  'city', 'country', 'job-position', 'company']
        for field in fields:
            if "success" not in self.get_field_class(field):
                return False
        return True

    @allure.step("Выполняет проверки после отправки формы")
    def check_form_submission(self) -> None:
        assert self.check_zip_code_error()
        assert self.check_fields_success()
