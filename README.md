### Проект автоматизации тестирования сервиса «Яндекс.Самокат»

## Описание

Этот проект содержит автоматизированные тесты для сервиса «Яндекс.Самокат» с использованием **Selenium WebDriver**. 

## Стек технологий

- **Python** — основной язык для написания тестов.
- **Selenium WebDriver** — для взаимодействия с браузером.
- **Pytest** — фреймворк для организации тестов и их выполнения.
- **Allure** - фреймворк для составления отчетов


## Установка

* Установить WebDriver
   Firefox https://www.selenium.dev/documentation/getting_started/installing_browser_drivers/


* Установить Selenium
   ```
   pip install selenium
   ```
* Установить Allure
   ```
   iwr -useb get.scoop.sh | iex
   ```
     ```
   scoop install allure
   ```
    Установить allure-pytest
    ```
   pip install allure-pytest
   ```

* Установка зависимостей:
    ```
    pip install -r requirements.txt
    ```


## Запуск тестов
  
* Команда для запуска всех тестов:
   ```
    pytest -v
   ```
  
## Запуск Allure

* Генерация отчета
   ```
    pytest tests.py --alluredir=allure_results 
   ```
