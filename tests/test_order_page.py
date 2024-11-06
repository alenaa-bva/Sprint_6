import allure
import pytest

from data import OrderPageData
from pages.scooter_order_page import ScooterOrderPage


class TestOrderPage:

    @pytest.mark.parametrize('customer_data', OrderPageData.set_of_customer_data)
    @allure.title('Проверка создания заказа')
    @allure.description('Открываем домашнюю страницу. \n'
                        'Нажимаем на кнопку заказать. \n'
                        'Заполняем форму заказа. \n'
                        'Размещаем заказ. \n'
                        'Проверяем, что появился номер заказа'
                        )
    def test_create_an_order(self, driver, customer_data):
        order_number = ScooterOrderPage.create_an_order(driver, customer_data)
        assert order_number is not None, "Номер заказа не найден"


