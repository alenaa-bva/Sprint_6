#здесь находятся локаторы и методы общих элементов
import time
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# общие методы
def wait_element_to_be_clickable(driver, locator, timeout=5):
    return WebDriverWait(driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

def wait_element_to_be_visible(driver, locator, timeout=5):
    return WebDriverWait(driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

def scroll_to_element(driver, locator):
    return driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(*locator))

def wait_element_to_be_invisible(driver, locator, timeout=5):
    return WebDriverWait(driver, timeout).until(expected_conditions.invisibility_of_element_located(locator))

class ScooterBasePage:

    def __init__(self, driver):
        self.driver = driver

    scooter_logo = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR') #лого самокат
    header_order_button = (By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']") #кнопка Заказать в хедере страницы
    order_status_button = (By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Статус заказа']") #кнопка Статус заказа
    order_number_input = (By.XPATH, ".//div[starts-with(@class, 'Header_SearchInput')]/div/input") #поле для номера заказа
    go_button = (By.XPATH, ".//button[text()='Go!']") #кнопка Go!
    close_cookies_modal_button = (By.ID, 'rcc-confirm-button') #кнопка закрытия модалки про куки

    def close_cookie_modal(self, driver):
        wait_element_to_be_clickable(driver, driver.find_element(*self.close_cookies_modal_button)).click()
        time.sleep(2)