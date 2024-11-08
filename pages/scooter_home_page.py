from selenium.webdriver.common.by import By
from locators import OrderPageLocators, HomePageLocators, BasePageLocators
from pages.scooter_base_page import ScooterBasePage


class ScooterHomePage(ScooterBasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_answer_by_click_on_question(self, driver):
        driver.get(BasePageLocators.home_page_url)

        self.wait_element_to_be_visible(driver, (By.XPATH, BasePageLocators.scooter_logo))

        self.close_cookie_modal()

        actual_questions_and_answers = {}

        #проверяем ответы на вопросы через цикл
        for question_xpath, answer_xpath  in zip(HomePageLocators.questions, HomePageLocators.answers):

            self.click_on_the_element(question_xpath)

            self.wait_element_to_be_visible(driver, (By.XPATH, answer_xpath))

            actual_question = driver.find_element(By.XPATH, question_xpath).text
            actual_answer = driver.find_element(By.XPATH, answer_xpath).text
            actual_questions_and_answers[actual_question.split('\n')[0]] = actual_answer

        return actual_questions_and_answers

    def move_to_dzen_page_by_click_on_yandex_logo(self, driver):
        driver.get(BasePageLocators.home_page_url)

        self.click_on_the_element(BasePageLocators.yandex_logo)

        #переход на страницу яндекс дзен
        self.switch_to_tab_with_url(driver, BasePageLocators.dzen_url)

        return self.wait_element_to_be_visible(driver, (By.XPATH, BasePageLocators.dzen_logo))

    def move_to_home_page_by_click_on_logo(self, driver, page):
        driver.get(page)

        self.click_on_the_element(BasePageLocators.scooter_logo)
        full_text = self.wait_element_to_be_visible(driver, (By.XPATH, HomePageLocators.header)).text

        # берем первую часть до разделителя
        return full_text.split('\n')[0]

    def move_to_create_an_order_page_from_home_page(self, driver, order_button):
        driver.get(BasePageLocators.home_page_url)

        self.wait_element_to_be_visible(driver, (By.XPATH, BasePageLocators.scooter_logo))

        self.close_cookie_modal()

        #переходим на страницу заказа
        self.click_on_the_element(order_button)

        return self.wait_element_to_be_visible(driver, (By.XPATH, OrderPageLocators.header_first_page)).text