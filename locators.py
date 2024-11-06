class BasePageLocators:
    #страницы
    home_page_url = "https://qa-scooter.praktikum-services.ru/"
    order_page_url = "https://qa-scooter.praktikum-services.ru/order"
    track_page_url = "https://qa-scooter.praktikum-services.ru/track"
    dzen_url = "https://dzen.ru"
    scooter_logo = ".//a[contains(@class, 'Header_LogoScooter')]"  # лого самокат
    yandex_logo = ".//a[contains(@class, 'Header_LogoYandex')]"  # лого яндекс
    header_order_button = ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']"  # кнопка Заказать в хедере страницы
    order_status_button = ".//div[starts-with(@class, 'Header')]/button[text()='Статус заказа']"  # кнопка Статус заказа
    order_number_input = ".//div[starts-with(@class, 'Header_SearchInput')]/div/input"  # поле для номера заказа
    close_cookies_modal_button = ".//button[contains(@class, 'App_CookieButton')]"  # кнопка закрытия модалки про куки
    dzen_logo = ".//a[contains(@class, 'dzen-layout--desktop-base-header__logoLink')]"  # лого яндекс дзен

class OrderPageLocators:
    header_first_page = ".//div[text()='Для кого самокат']" #Заголовок "Для кого самокат"
    first_name_field = ".//div[@class='Order_Form__17u6u']/div[@class='Input_InputContainer__3NykH'][1]/input" # поле Имя
    last_name_field = ".//div[@class='Order_Form__17u6u']/div[@class='Input_InputContainer__3NykH'][2]/input"# поле Фамилия
    address_field = ".//div[@class='Order_Form__17u6u']/div[@class='Input_InputContainer__3NykH'][3]/input" # поле Адрес
    metro_station_menu = ".//div[@class='select-search__select']" #список станций
    metro_station_field = ".//div[@class='select-search__value']/input[@class='select-search__input']" # Поле станция метро
    metro_station_list = ".//ul[@class='select-search__options']/li[@class='select-search__row']" #список станций
    phone_field = ".//div[@class='Order_Form__17u6u']/div[@class='Input_InputContainer__3NykH'][4]/input" # Поле Телефон
    next_button = ".//div/button[@class='Button_Button__ra12g Button_Middle__1CSJM']" # Кнопка Далее

    header_second_page = ".//div[text()='Про аренду']" # заголовок "Про аренду"
    date_field = ".//div[@class='react-datepicker__input-container']"# поле Даты
    date_list = ".//div[@role='button']" # виджет календаря
    rental_period_field = ".//div[@class='Dropdown-control']/div[@class='Dropdown-placeholder']" # Поле Срок аренды
    rental_period_menu = ".//div[@class='Dropdown-root is-open']/div[@class='Dropdown-menu']" # меню срока аренды
    rental_period_list = ".//div[@class='Dropdown-root is-open']/div[@class='Dropdown-menu']/div[@role='option']" # список сроков аренды
    color_list = ".//label[@class='Checkbox_Label__3wxSf']" # список цветов
    comment_field = ".//div[@class='Order_Form__17u6u']/div[@class='Input_InputContainer__3NykH']/input" # поле Комментарий
    make_an_order_button = ".//div[@class='Order_Buttons__1xGrp']/button[2]" # Кнопка завершения заказа
    modal_yes_button = ".//div[@class='Order_Modal__YZ-d3']/div[@class='Order_Buttons__1xGrp']/button[2]" # Кнопка "Да" на модалке подтверждения заказа
    order_number = ".//div[@class='Order_Text__2broi']" #номер заказа
    order_page_header = ".//div[@class='Order_Header__BZXOb']" #хедер на странице заказа

class HomePageLocators:
    header = ".//div[@class='Home_Header__iJKdX' and contains(text(), 'Самокат')]" # Заголовок, начинающийся с "Самокат"
    middle_order_button = ".//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']" # кнопка Заказать внизу страницы
    questions_data = [
        ".//div[@class='accordion']/div[1]",
        ".//div[@class='accordion']/div[2]",
        ".//div[@class='accordion']/div[3]",
        ".//div[@class='accordion']/div[4]",
        ".//div[@class='accordion']/div[5]",
        ".//div[@class='accordion']/div[6]",
        ".//div[@class='accordion']/div[7]",
        ".//div[@class='accordion']/div[8]"
    ] # вопросы о важном
    answers = [
        ".//div[@class='accordion']/div[1]/div[@class='accordion__panel']/p",
        ".//div[@class='accordion']/div[2]/div[@class='accordion__panel']/p",
        ".//div[@class='accordion']/div[3]/div[@class='accordion__panel']/p",
        ".//div[@class='accordion']/div[4]/div[@class='accordion__panel']/p",
        ".//div[@class='accordion']/div[5]/div[@class='accordion__panel']/p",
        ".//div[@class='accordion']/div[6]/div[@class='accordion__panel']/p",
        ".//div[@class='accordion']/div[7]/div[@class='accordion__panel']/p",
        ".//div[@class='accordion']/div[8]/div[@class='accordion__panel']/p"
    ] # ответы на вопросы

