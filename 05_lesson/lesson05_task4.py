from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")
print('http')

username_input = driver.find_element(By.CSS_SELECTOR, "input#username")
print('username_input')

entering_username = username_input.send_keys("tomsmith")
print('tomsmith')

password_input = driver.find_element(By.CSS_SELECTOR, "input#password")
print('password_input')

entering_password = password_input.send_keys("SuperSecretPassword!")
print('SuperSecretPassword!')

login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
print('login')

login_button.click()
print('click')

text = driver.find_element(By.CSS_SELECTOR, ".flash.success").text
print(text)

driver.quit()
print('quit')
