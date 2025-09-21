from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 200)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def waiting_loading_main_page(self):
        self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "input#user-name"))
        )

    def authorization_standard_user(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "input#user-name").send_keys("standard_user")
        self.driver.find_element(
            By.CSS_SELECTOR, "input#password").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "input#login-button").click()

    def waiting_loading_products_page(self):
        self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack"))
        )

    def add_item_to_cart(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-bolt-t-shirt"
                ).click()
        self.driver.find_element(
            By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-onesie").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "a.shopping_cart_link").click()

    def waiting_loading_your_cart_page(self):
        self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "button#checkout"))
        )

    def button_checkout_click(self):
        checkout = self.driver.find_element(By.CSS_SELECTOR, "button#checkout")
        self.driver.execute_script("arguments[0].scrollIntoView();", checkout)
        checkout.click()

    def waiting_loading_your_information_page(self):
        self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "input#first-name"))
        )

    def input_your_data(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "input#first-name").send_keys("Natalia")
        self.driver.find_element(
            By.CSS_SELECTOR, "input#last-name").send_keys("Vasileva")
        self.driver.find_element(
            By.CSS_SELECTOR, "input#postal-code").send_keys("662311")
        self.driver.find_element(By.CSS_SELECTOR, "input#continue").click()

    def waiting_loading_checkout_overview_page(self):
        self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div.summary_total_label"))
        )

    def get_total(self):
        return self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text

    def quit(self):
        self.driver.quit()
