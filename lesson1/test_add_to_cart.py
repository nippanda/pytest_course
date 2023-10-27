from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()



def test_add_item_to_the_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    item_to_be_added = driver.find_element(By.CSS_SELECTOR, '#item_4_title_link').text

    button_add_to_cart = driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]')
    button_add_to_cart.click()

    go_to_cart = driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a')
    go_to_cart.click()

    item_added = driver.find_element(By.CSS_SELECTOR, '#item_4_title_link').text

    assert item_to_be_added == item_added

    driver.quit()