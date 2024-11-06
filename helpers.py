from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def switch_to_tab_with_url(driver, expected_url, timeout=5):
    WebDriverWait(driver, timeout).until(expected_conditions.number_of_windows_to_be(2))
    all_windows = driver.window_handles
    current_window = driver.current_window_handle

    for window in all_windows:
        if window != current_window:
            driver.switch_to.window(window)
            WebDriverWait(driver, timeout).until(expected_conditions.url_contains(expected_url))
        else:
            driver.switch_to.window(current_window)

def wait_element_to_be_clickable(driver, locator, timeout=5):
    return WebDriverWait(driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

def wait_element_to_be_visible(driver, locator, timeout=5):
    return WebDriverWait(driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

def scroll_to_element(driver, xpath):
    element = driver.find_element(By.XPATH, xpath)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    wait_element_to_be_visible(driver, (By.XPATH, xpath))

def click_on_the_element(driver, element):
    scroll_to_element(driver, element)
    wait_element_to_be_clickable(driver, (By.XPATH, element))
    driver.find_element(By.XPATH, element).click()
