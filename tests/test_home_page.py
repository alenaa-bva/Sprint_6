from asyncio import wait_for
from time import sleep

from selenium import webdriver

from pages.scooter_base_page import ScooterBasePage, wait_element_to_be_visible, scroll_to_element
from pages.scooter_home_page import ScooterHomePage


class TestHomePage:
    def test_get_answer_by_click_on_question(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')

        scooter_base_page = ScooterBasePage(driver)
        scooter_home_page = ScooterHomePage(driver)

        #ждем загрузки страницы
        wait_element_to_be_visible(driver, scooter_base_page.scooter_logo)

        #закрываем модалку про куки
        scooter_base_page.close_cookie_modal(driver)

        #проскроллить до элемента
        scroll_to_element(driver, scooter_home_page.question_1)

        #нажать на вопрос о важном, проверить ответ на вопрос
        scooter_home_page.click_question_button()

        wait_element_to_be_visible(driver, scooter_home_page.answer_1)

        expected = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        assert scooter_home_page.answer_1.text == expected