import time
from selenium.webdriver.common.by import By
from helpers import wait_element_to_be_clickable, scroll_to_element
from locators import BasePageLocators

class ScooterBasePage:
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def close_cookie_modal(driver):
        wait_element_to_be_clickable(driver, (By.XPATH, BasePageLocators.close_cookies_modal_button)).click()
        time.sleep(2)

    def click_on_the_element(self, element):
        scroll_to_element(self.driver, element)
        wait_element_to_be_clickable(self.driver, (By.XPATH, element))
        self.driver.find_element(By.XPATH, element).click()