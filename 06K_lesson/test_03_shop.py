from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Edge()

    driver.get("https://www.saucedemo.com/")
    waiter = WebDriverWait(driver, 100)
    waiter.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input#user-name"))
    )

    driver.find_element(By.CSS_SELECTOR, "input#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "input#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "input#login-button").click()

    waiter = WebDriverWait(driver, 20)
    waiter.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack"))
    )

    driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()

    waiter = WebDriverWait(driver, 20)
    waiter.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button#checkout"))
    )

    checkout = driver.find_element(By.CSS_SELECTOR, "button#checkout")
    driver.execute_script("arguments[0].scrollIntoView();", checkout)
    checkout.click()

    waiter = WebDriverWait(driver, 20)
    waiter.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input#first-name"))
    )

    driver.find_element(By.CSS_SELECTOR, "input#first-name").send_keys("Natalia")
    driver.find_element(By.CSS_SELECTOR, "input#last-name").send_keys("Vasileva")
    driver.find_element(By.CSS_SELECTOR, "input#postal-code").send_keys("662311")
    driver.find_element(By.CSS_SELECTOR, "input#continue").click()

    waiter = WebDriverWait(driver, 20)
    waiter.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.summary_total_label"))
    )

    total = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text

    driver.quit()

    assert total == "Total: $58.29"
