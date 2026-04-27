import allure
from pages.main_page import MainPage
from helpers.urls import Url


class TestMain:

    @allure.title('переход на «Конструктор»')
    def test_go_to_constructor(self, browser):
        page = MainPage(browser)
        page.go_to_constructor()
        actual_url = browser.current_url
        expected_base = Url.BASE_URL
        assert actual_url.startswith(expected_base), \
            f"Текущий URL {actual_url} не начинается с {expected_base}"    

    @allure.title('переход на раздел «Лента заказов»')
    def test_go_to_feed(self, browser):
        page = MainPage(browser)
        page.go_to_feed()
        assert page.get_current_url() == Url.FEED_URL

    @allure.title('Открытие всплывающего окна ингредиента')
    def test_open_ingredient_modal(self, browser):
        page = MainPage(browser)
        page.open_ingredient_modal()
        assert page.modal_open()

    @allure.title('Закрытие всплывающего окна по крестику')
    def test_close_ingredient_modal(self, browser):
        page = MainPage(browser)
        page.open_ingredient_modal()
        page.close_ingredient_modal()
        assert page.modal_closed()

    @allure.title('Счётчик ингредиента увеличивается')
    def test_ingredient_counter(self, browser):
        page = MainPage(browser)
        page.open_page(Url.BASE_URL)
        initial = int(page.get_sauce_counter() or 0)
        page.add_bun()
        page.add_sauce()
        final = int(page.get_sauce_counter() or 0)
        assert final > initial
