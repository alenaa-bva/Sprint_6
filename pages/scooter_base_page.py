import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import BasePageLocators

class ScooterBasePage:
    def __init__(self, driver):
        self.driver = driver

    def close_cookie_modal(self):
        self.wait_element_to_be_clickable(self.driver, (By.XPATH, BasePageLocators.close_cookies_modal_button)).click()
        time.sleep(2)

    def click_on_the_element(self, element):
        self.scroll_to_element(self.driver, element)
        self.wait_element_to_be_clickable(self.driver, (By.XPATH, element))
        self.driver.find_element(By.XPATH, element).click()

    def switch_to_tab_with_url(self, driver, expected_url, timeout=5):
        WebDriverWait(driver, timeout).until(expected_conditions.number_of_windows_to_be(2))
        all_windows = driver.window_handles
        current_window = driver.current_window_handle

        for window in all_windows:
            if window != current_window:
                driver.switch_to.window(window)
                WebDriverWait(driver, timeout).until(expected_conditions.url_contains(expected_url))
            else:
                driver.switch_to.window(current_window)

    def wait_element_to_be_clickable(self, driver, locator, timeout=5):
        return WebDriverWait(driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    def wait_element_to_be_visible(self, driver, locator, timeout=5):
        return WebDriverWait(driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def scroll_to_element(self, driver, xpath):
        element = driver.find_element(By.XPATH, xpath)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait_element_to_be_visible(driver, (By.XPATH, xpath))
