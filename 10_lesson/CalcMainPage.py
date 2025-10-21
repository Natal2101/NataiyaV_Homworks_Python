from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalcMainPage:
    """"
        Класс для работы с главной страницей калькулятора.
        Этот класс предоставляет методы для взаимодействия с калькулятором,
        включает установку задержки, нажатие кнопок, ожидание результата и
        получение результата.
    """


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)

    @allure.step("Открывает страницу калькулятора в браузере по заданному URL")
    def open(self) -> None:
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/"
                        "slow-calculator.html")

    @allure.step("Устанавливает {delay} секунд задержки в поле ввода")
    def set_delay(self, delay: int) -> None:
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    @allure.step("Нажимает кнопку {button} калькулятора "
                 "по её текстовому содержимому")
    def click_button(self, button: str) -> None:
        self.driver.find_element(
            By.XPATH, f"//span[text()='{button}']").click()

    @allure.step("Последовательно нажимает кнопки {buttons} калькулятора")
    def click_buttons(self, buttons: list[str]) -> None:
        for button in buttons:
            self.click_button(button)

    @allure.step("Ожидает появления ожидаемого результата "
                 "на экране калькулятора. Добавляет к задержке "
                 "в {delay} секунд +1 секунду для надежности")
    def wait_for_result(self, expected_result: str, delay: int) -> None:
        # Добавляем +1 секунду к задержке для надежности
        WebDriverWait(self.driver, delay + 1).until(
            EC.text_to_be_present_in_element((
                By.CLASS_NAME, "screen"), expected_result)
        )

    @allure.step("Получает и возвращает значение результата "
                 "с экрана калькулятора")
    def get_result(self) -> str:
        return self.driver.find_element(By.CLASS_NAME, "screen").text
