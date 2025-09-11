from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")
print('http')

sky_input = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
print('sky_input')

entering_sky = sky_input.send_keys("Sky")
print('entering_sky')

sky_input.clear()
print('clear')

entering_pro = sky_input.send_keys("Pro")
print('entering_pro')

driver.quit()
print('quit')
