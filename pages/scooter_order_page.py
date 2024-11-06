import random
from selenium.webdriver.common.by import By
from helpers import wait_element_to_be_visible, wait_element_to_be_clickable
from locators import OrderPageLocators, BasePageLocators
from pages.scooter_base_page import ScooterBasePage


class ScooterOrderPage:
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def create_an_order(driver, set_of_customer_data):
        driver.get(BasePageLocators.home_page_url)

        scooter_base_page_object = ScooterBasePage(driver)

        wait_element_to_be_visible(driver, (By.XPATH, BasePageLocators.scooter_logo))

        ScooterBasePage.close_cookie_modal(driver)

        # переходим на страницу заказа
        scooter_base_page_object.click_on_the_element(BasePageLocators.header_order_button)
        wait_element_to_be_visible(driver, (By.XPATH, OrderPageLocators.header_first_page))

        driver.find_element(By.XPATH, OrderPageLocators.first_name_field).send_keys(set_of_customer_data["first_name"])
        driver.find_element(By.XPATH, OrderPageLocators.last_name_field).send_keys(set_of_customer_data["last_name"])
        driver.find_element(By.XPATH, OrderPageLocators.address_field).send_keys(set_of_customer_data["address"])
        ScooterOrderPage.random_metro_station(driver)
        driver.find_element(By.XPATH, OrderPageLocators.phone_field).send_keys(set_of_customer_data["phone"])
        driver.find_element(By.XPATH, OrderPageLocators.next_button).click()

        wait_element_to_be_visible(driver, (By.XPATH, OrderPageLocators.header_second_page))

        ScooterOrderPage.random_date(driver)
        ScooterOrderPage.random_rental_period(driver)
        ScooterOrderPage.random_color(driver)
        driver.find_element(By.XPATH, OrderPageLocators.comment_field).send_keys(set_of_customer_data["comment"])
        driver.find_element(By.XPATH, OrderPageLocators.make_an_order_button).click()
        wait_element_to_be_clickable(driver, (By.XPATH, OrderPageLocators.modal_yes_button))
        driver.find_element(By.XPATH, OrderPageLocators.modal_yes_button).click()

        wait_element_to_be_visible(driver, (By.XPATH, OrderPageLocators.order_number))

        return OrderPageLocators.order_number

    @staticmethod
    def random_metro_station(driver):
        driver.find_element(By.XPATH, OrderPageLocators.metro_station_field).click()
        metro_station_list = driver.find_elements(By.XPATH, OrderPageLocators.metro_station_list)
        random_metro_station = random.choice(metro_station_list)
        driver.execute_script("arguments[0].scrollIntoView();", random_metro_station)
        random_metro_station.click()

    @staticmethod
    def random_date(driver):
        driver.find_element(By.XPATH, OrderPageLocators.date_field).click()
        date_list = driver.find_elements(By.XPATH, OrderPageLocators.date_list)
        random_date = random.choice(date_list)
        driver.execute_script("arguments[0].scrollIntoView();", random_date)
        random_date.click()

    @staticmethod
    def random_rental_period(driver):
        driver.find_element(By.XPATH, OrderPageLocators.rental_period_field).click()
        rental_period_list = driver.find_elements(By.XPATH, OrderPageLocators.rental_period_list)
        random_rental_period = random.choice(rental_period_list)
        driver.execute_script("arguments[0].scrollIntoView();", random_rental_period)
        random_rental_period.click()

    @staticmethod
    def random_color(driver):
        random_color_list = driver.find_elements(By.XPATH, OrderPageLocators.color_list)
        random_color = random.choice(random_color_list)
        driver.execute_script("arguments[0].scrollIntoView();", random_color)
        random_color.click()
