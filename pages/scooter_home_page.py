from selenium.webdriver.common.by import By
from locators import OrderPageLocators, HomePageLocators, BasePageLocators
from helpers import switch_to_tab_with_url, wait_element_to_be_visible
from pages.scooter_base_page import ScooterBasePage


class ScooterHomePage:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def get_answer_by_click_on_question(driver, index = 0):
        driver.get(BasePageLocators.home_page_url)

        scooter_base_page_object = ScooterBasePage(driver)

        wait_element_to_be_visible(driver, (By.XPATH, BasePageLocators.scooter_logo))

        ScooterBasePage.close_cookie_modal(driver)

        actual_answers = []

        #проверяем ответы на вопросы через цикл
        for question_xpath, answer_xpath  in zip(HomePageLocators.questions_data, HomePageLocators.answers):

            scooter_base_page_object.click_on_the_element(question_xpath)

            wait_element_to_be_visible(driver, (By.XPATH, answer_xpath))

            actual = driver.find_element(By.XPATH, answer_xpath).text
            actual_answers.append(actual)

            index+=1

        return actual_answers

    @staticmethod
    def move_to_dzen_page_by_click_on_yandex_logo(driver):
        driver.get(BasePageLocators.home_page_url)

        scooter_base_page_object = ScooterBasePage(driver)

        scooter_base_page_object.click_on_the_element(BasePageLocators.yandex_logo)

        #переход на страницу яндекс дзен
        switch_to_tab_with_url(driver, BasePageLocators.dzen_url)

        return wait_element_to_be_visible(driver, (By.XPATH, BasePageLocators.dzen_logo))

    @staticmethod
    def move_to_home_page_by_click_on_logo(driver, page):
        driver.get(page)

        scooter_base_page_object = ScooterBasePage(driver)

        scooter_base_page_object.click_on_the_element(BasePageLocators.scooter_logo)
        full_text = wait_element_to_be_visible(driver, (By.XPATH, HomePageLocators.header)).text

        # берем первую часть до разделителя
        return full_text.split('\n')[0]

    @staticmethod
    def move_to_create_an_order_page_from_home_page(driver, order_button):
        driver.get(BasePageLocators.home_page_url)

        scooter_base_page_object = ScooterBasePage(driver)

        wait_element_to_be_visible(driver, (By.XPATH, BasePageLocators.scooter_logo))

        ScooterBasePage.close_cookie_modal(driver)

        #переходим на страницу заказа
        scooter_base_page_object.click_on_the_element(order_button)

        return wait_element_to_be_visible(driver, (By.XPATH, OrderPageLocators.header_first_page)).text