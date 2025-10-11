from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class ShopPage:
    """
        Класс для работы с веб-страницей магазина Sauce Demo.
        Этот класс предоставляет методы для взаимодействия с магазином.
        Включает в себя: открытие страницы в браузере, авторизацию,
        добавление товаров в корзину, ввод данных и получение итоговой суммы.
    """

    @allure.step("Инициализирует экземпляр страницы. "
                 "Параметр driver: WebDriver")
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 200)

    @allure.step("Открывает главную страницу интернет-магазина "
                 "по указанному url")
    def open(self) -> None:
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Ожидает загрузки главной страницы, "
                 "конкретно - появления поля ввода имени пользователя")
    def waiting_loading_main_page(self) -> None:
        self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "input#user-name"))
        )

    @allure.step("Выполняет авторизацию стандартного пользователя, "
                 "вводя логин и пароль")
    def authorization_standard_user(self) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, "input#user-name").send_keys("standard_user")
        self.driver.find_element(
            By.CSS_SELECTOR, "input#password").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "input#login-button").click()

    @allure.step("Ожидает загрузки страницы товаров, "
                 "конкретно - появления кнопки добавления в корзину")
    def waiting_loading_products_page(self) -> None:
        self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack"))
        )

    @allure.step("Добавляет три товара в корзину и переходит в корзину")
    def add_item_to_cart(self) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-bolt-t-shirt"
                ).click()
        self.driver.find_element(
            By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-onesie").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "a.shopping_cart_link").click()

    @allure.step("Ожидает загрузки страницы корзины, "
                 "конкретно - появления кнопки оформления заказа")
    def waiting_loading_your_cart_page(self) -> None:
        self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "button#checkout"))
        )

    @allure.step("Прокручивает страницу к кнопке оформления заказа "
                 "и нажимает на нее")
    def button_checkout_click(self) -> None:
        checkout = self.driver.find_element(By.CSS_SELECTOR, "button#checkout")
        self.driver.execute_script("arguments[0].scrollIntoView();", checkout)
        checkout.click()

    @allure.step("Ожидает загрузки страницы ввода информации, "
                 "конкретно - появления поля имени")
    def waiting_loading_your_information_page(self) -> None:
        self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "input#first-name"))
        )

    @allure.step("Заполняет поля персональной информации покупателя: "
                 "имя: {first_name}, "
                 "фамилия: {last_name}, "
                 "индекс: {postal_code}")
    def input_your_data(self, first_name, last_name, postal_code) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, "input#first-name").send_keys(first_name)
        self.driver.find_element(
            By.CSS_SELECTOR, "input#last-name").send_keys(last_name)
        self.driver.find_element(
            By.CSS_SELECTOR, "input#postal-code").send_keys(postal_code)
        self.driver.find_element(By.CSS_SELECTOR, "input#continue").click()

    @allure.step("Ожидает загрузки страницы обзора заказа,"
                 "конкретно - появления итоговой суммы")
    def waiting_loading_checkout_overview_page(self) -> None:
        self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div.summary_total_label"))
        )

    @allure.step("Получает и возвращает итоговую сумму заказа")
    def get_total(self) -> str:
        return self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text
