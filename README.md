# Diplom_3
### Автотесты для UI, веб-приложение Stellar Burgers. 
#### Проверка корректность работы ключевых сценариев в браузерах Chrome и Firefox с использованием паттерна Page Object Model (POM) и отчётности Allure.

#### Стек технологий:
Python 3.14;    
PyTest;
Selenium WebDriver;   
Page Object Model;       
requests;   
Allure;     
Faker.  

#### Функционал тестов:     
* Навигация:
    - переход в раздел «Конструктор» по клику на соответствующий элемент;
    - переход в раздел «Лента заказов» по клику на соответствующий элемент.
* Работа с ингредиентами:
    - открытие всплывающего окна с деталями ингредиента при клике на него;
    - закрытие всплывающего окна кликом по крестику.
* Оформление заказа и лента заказов:
    - создание нового заказа через кнопку «Оформить заказ»;
    - появление номера заказа в разделе «В работе» после оформления;
    - увеличение счётчика «Выполнено за всё время» при создании нового заказа;
    - увеличение счётчика «Выполнено за сегодня» при создании нового заказа.

#### Запуск тестов:
Запуск тесов с измерением покрытия кода (100%):      
`pytest --cov=. --cov-fail-under=100 --cov-report=html --cov-report=term-missing tests/`

Генерация отчёта Allure:    
в браузере Сhrome - `pytest tests/ --alluredir=allure_results_chrome --browser chrome`  
в браузере Firefox -  `pytest tests/ --alluredir=allure_results_firefox --browser firefox`    

Просмотр отчёта Allure:     
Сhrome - `allure serve allure_results/`  
Firefox - `allure serve allure_results/`  