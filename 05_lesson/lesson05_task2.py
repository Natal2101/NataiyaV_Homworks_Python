
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/dynamicid/")
print('http')

blue_button = (driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']"))
print('blue_button')

blue_button.click()
print('click')

driver.quit()
print('quit')
