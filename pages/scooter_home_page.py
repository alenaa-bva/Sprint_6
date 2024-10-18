#Нажать кнопку «Заказать». На странице две кнопки заказа.
from selenium.webdriver.common.by import By


class ScooterHomePage:
    middle_order_button = (By.XPATH, ".//button[contains(@class, 'Middle') and text()='Заказать']") # кнопка Заказать внизу страницы
    question_1 = (By.XPATH, ".//div[@class='accordion']/div[1]/div/div[@class='accordion__button']") # вопрос о важном
    answer_1 = (By.XPATH, ".//div[@class='accordion']/div[1]/div[@class='accordion__panel']/p") # ответ на вопрос

    def __init__(self, driver):
        self.driver = driver

    # нажать на кнопку Заказать внизу страницы

    def click_middle_order_button(self):
        self.driver.find_element(*self.middle_order_button).click()

    # нажать на вопрос о важном

    def click_question_button(self):
        self.driver.find_element(*self.question_1).click()

