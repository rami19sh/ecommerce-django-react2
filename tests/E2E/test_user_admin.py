import time
from select import select
from selenium.common import NoSuchElementException, ElementNotInteractableException, TimeoutException, \
    StaleElementReferenceException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome import webdriver
# from selenium.webdriver.firefox import webdriver

# from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

import pytest


@pytest.fixture()
def driver():
    # chrome_driver_binary = r"./chromedriver"
    # ser_chrome = ChromeService(chrome_driver_binary)
    driver = webdriver.Chrome(ChromeDriverManager().install())

    yield driver
    driver.close()

def test_update_price_of_product(driver):
        driver.get("http://127.0.0.1:8000/#/")
        driver.set_window_size(1552, 840)
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div:nth-child(3) > div > div:nth-child(1) > div > a > img").click()
        time.sleep(5)
        driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
        driver.set_window_size(1552, 840)
        time.sleep(2)
        driver.find_element(By.ID, "id_username").send_keys("rami19shehk@gmail.com")
        driver.find_element(By.ID, "id_password").send_keys("991594123rami")
        driver.find_element(By.ID, "id_password").send_keys(Keys.ENTER)
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, "Products").click()
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, "iPhone 13 128GB | Apple | 899.00").click()
        time.sleep(3)
        driver.find_element(By.ID, "id_price").click()
        time.sleep(3)
        element = driver.find_element(By.ID, "id_price")
        actions = ActionChains(driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = driver.find_element(By.ID, "id_price")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        element = driver.find_element(By.ID, "id_price")
        actions = ActionChains(driver)
        actions.move_to_element(element).release().perform()
        driver.find_element(By.ID, "id_price").click()
        driver.find_element(By.ID, "id_price").clear()
        driver.find_element(By.ID, "id_price").send_keys("849.00")
        time.sleep(3)
        driver.find_element(By.NAME, "_save").click()
        time.sleep(3)
        driver.get("http://127.0.0.1:8000/#/")
        driver.set_window_size(1552, 840)
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,
                            "#root > div > main > div > div:nth-child(3) > div > div:nth-child(1) > div > a > img").click()
        time.sleep(2)
        new_price=driver.find_element(By.CSS_SELECTOR,"#root > div > main > div > div > div:nth-child(1) > div.col-md-3 > div > div:nth-child(3)").text
        assert "849" in new_price
        time.sleep(3)

# def test_buy_product(driver):
#     driver.get("http://127.0.0.1:8000/#/")
#     driver.set_window_size(1552, 840)
#     driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
#     time.sleep(2)
#     driver.find_element(By.ID, "email").click()
#     time.sleep(2)
#     driver.find_element(By.ID, "email").send_keys("sami1992@gmail.com")
#     driver.find_element(By.ID, "password").send_keys("rami991594123")
#     driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
#     time.sleep(3)
#     element = driver.find_element(By.CSS_SELECTOR, ".active .carousel\\.caption")
#     actions = ActionChains(driver)
#     actions.move_to_element(element).perform()
#     time.sleep(3)
#     element = driver.find_element(By.CSS_SELECTOR, ".active .carousel\\.caption")
#     actions = ActionChains(driver)
#     actions.move_to_element(element).perform()
#     time.sleep(3)
#     element = driver.find_element(By.CSS_SELECTOR, "body")
#     # actions = ActionChains(driver)
#     # actions.move_to_element(element, 0, 0).perform()
#     driver.find_element(By.CSS_SELECTOR, ".col-xl-3:nth-child(2) .card-img").click()
#     time.sleep(3)
#     driver.execute_script("window.scrollTo(0,200)")
#     driver.find_element(By.CSS_SELECTOR, ".w-100").click()
#     time.sleep(3)
#     driver.execute_script("window.scrollTo(0,61.599998474121094)")
#     driver.find_element(By.CSS_SELECTOR, ".w-100").click()
#     time.sleep(2)
#     driver.find_element(By.CSS_SELECTOR, "#address").click()
#     driver.find_element(By.CSS_SELECTOR, "#address").clear()
#     driver.find_element(By.CSS_SELECTOR, "#address").send_keys("ben ami")
#     driver.find_element(By.CSS_SELECTOR, "#city").click()
#     driver.find_element(By.CSS_SELECTOR, "#city").clear()
#     driver.find_element(By.CSS_SELECTOR, "#city").send_keys("akko")
#     driver.find_element(By.CSS_SELECTOR, "#postalCode").click()
#     driver.find_element(By.CSS_SELECTOR, "#postalCode").clear()
#     driver.find_element(By.CSS_SELECTOR, "#postalCode").send_keys("2460417")
#     driver.find_element(By.CSS_SELECTOR, "#country").click()
#     driver.find_element(By.CSS_SELECTOR, "#country").clear()
#     driver.find_element(By.CSS_SELECTOR, "#country").send_keys("israel")
#     time.sleep(3)
#     driver.find_element(By.CSS_SELECTOR, ".my-3").click()
#     time.sleep(3)
#     driver.find_element(By.CSS_SELECTOR, ".my-3").click()
#     time.sleep(3)
#     driver.find_element(By.CSS_SELECTOR, ".w-100").click()
#     time.sleep(3)
#     order_summ=driver.find_element(By.CSS_SELECTOR,"#root > div > main > div > div > div.col-md-4 > div > div > div:nth-child(1) > h2")
#     assert order_summ.is_displayed() ==True


# def test_positive_login(driver):
#     driver.get("http://127.0.0.1:8000/#/")
#     driver.set_window_size(1552, 840)
#     driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
#     time.sleep(2)
#     driver.find_element(By.ID, "email").click()
#     time.sleep(2)
#     driver.find_element(By.ID, "email").send_keys("sami1992@gmail.com")
#     driver.find_element(By.ID, "password").send_keys("rami991594123")
#     driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
#     time.sleep(3)
#     selector_login=driver.find_element(By.CSS_SELECTOR,"#username")
#     assert selector_login.is_displayed()
# #
# #
# #
# def test_nigative_login(driver):
#     driver.get("http://127.0.0.1:8000/#/")
#     driver.set_window_size(1552, 840)
#     driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
#     time.sleep(2)
#     driver.find_element(By.ID, "email").click()
#     time.sleep(2)
#     driver.find_element(By.ID, "email").send_keys("sami122@gmail.com")
#     driver.find_element(By.ID, "password").send_keys("rami991594123")
#     driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
#     time.sleep(3)
#     error_msg=driver.find_element(By.CSS_SELECTOR,"#root > div > main > div > div > div > div.fade.alert.alert-danger.show")
#     assert "no active account found" in error_msg.text.lower()
