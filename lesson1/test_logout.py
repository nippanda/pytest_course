from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()



def test_logout():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    burger_menu = driver.find_element(By.ID, 'react-burger-menu-btn')
    burger_menu.click()

    burger_menu_logout_button = driver.find_element(By.ID, 'logout_sidebar_link')
    burger_menu_logout_button.click()

    time.sleep(5)
    assert driver.current_url == "https://www.saucedemo.com/"

    driver.quit()
