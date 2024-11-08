import allure
import pytest
from data import HomePageData
from locators import HomePageLocators, BasePageLocators
from pages.scooter_home_page import ScooterHomePage


class TestHomePage:
    @allure.title('Проверка блока "Вопросы о важном"')
    @allure.description('Открываем домашнюю страницу. \n'
                        'Переходим к блоку "Вопросы о важном". \n'
                        'Нажимаем на вопрос. \n'
                        'Проверяем, что появился ожидаемый вопрос . \n'
                        'Проверяем, что появился соответствующий ответ на вопрос.'
                        )
    def test_get_answer_by_click_on_question(self, driver):

        scooter_home_page_object = ScooterHomePage(driver)
        expected_questions = HomePageData.QUESTIONS_DATA
        expected_answers = HomePageData.ANSWERS_DATA

        actual_questions_and_answers = scooter_home_page_object.get_answer_by_click_on_question(driver)

        for actual_question, actual_answer in actual_questions_and_answers.items():
            # Проверяем, что вопрос есть в списке ожидаемых
            assert actual_question in expected_questions, f"Вопрос '{actual_question}' не найден среди ожидаемых"

            # Выясняем какой индекс у вопроса в списке ожидаемых вопросов
            index_of_question = expected_questions.index(actual_question)

            # Проверяем ответ по найденному индексу вопроса
            assert expected_answers[index_of_question] == actual_answer, f"Ответ {actual_answer} не соответствует вопросу '{actual_question}'"





    @pytest.mark.parametrize('order_button',
                             [
                                 HomePageLocators.middle_order_button,
                                 BasePageLocators.header_order_button
                             ])
    @allure.title('Проверка перехода с домашней страницы на страницу заказа')  # декораторы
    @allure.description('Открываем домашнюю страницу. \n'
                        'Нажимаем на кнопку заказать. \n'
                        'Проверяем, что перешли на страницу заказа.'
                        )
    def test_move_to_create_an_order_page_from_home_page(self, driver, order_button):

        scooter_home_page_object = ScooterHomePage(driver)
        actual = scooter_home_page_object.move_to_create_an_order_page_from_home_page(driver, order_button)
        expected = 'Для кого самокат'
        assert actual == expected, f"Заголовок '{expected}' не найден."


    @pytest.mark.parametrize('page',
                             [
                                 BasePageLocators.home_page_url,
                                 BasePageLocators.order_page_url,
                                 BasePageLocators.track_page_url
                             ])
    @allure.title('Проверка перехода на домашнюю страницу по клику на логотип "Самокат"')
    @allure.description('Открываем страницу Самоката, отличную от домашней страницы. \n'
                        'Нажимаем на логотип "Самокат". \n'
                        'Проверяем, что перешли на домашнюю страницу.'
                        )
    def test_move_to_home_page_by_click_on_logo(self, driver, page):

        scooter_home_page_object = ScooterHomePage(driver)
        actual = scooter_home_page_object.move_to_home_page_by_click_on_logo(driver,page)
        expected = 'Самокат'
        assert actual == expected, f"Заголовок '{expected}...' не найден."

    @allure.title('Проверка перехода на яндекс.дзен по клику на логотип "Яндекс"')
    @allure.description('Открываем домашнюю страницу. \n'
                        'Нажимаем на логотип "Яндекс". \n'
                        'Проверяем, что перешли на новую вкладку сайта яндекс.дзен.'
                        )
    def test_move_to_dzen_page_by_click_on_yandex_logo(self, driver):

        scooter_home_page_object = ScooterHomePage(driver)
        dzen_logo = scooter_home_page_object.move_to_dzen_page_by_click_on_yandex_logo(driver)
        assert dzen_logo is not None, "Логотип 'дзен' не найден."



