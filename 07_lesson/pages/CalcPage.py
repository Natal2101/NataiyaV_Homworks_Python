from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 45)

    def open(self):
        self.driver.get(
            'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'
            )

    def input_45(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#delay").clear()
        self.driver.find_element(
            By.CSS_SELECTOR, "#delay").send_keys("45")

    def input_numbers(self):
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    def wait_45_seconds(self):
        self.wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "div.screen"), "15")
        )

    def get_result(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.screen").text
