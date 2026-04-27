import allure
from helpers.urls import Url
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Перейти в «Конструктор»')
    def go_to_constructor(self):
        self.open_page(Url.FEED_URL)
        self._click_outside_modal()
        super().go_to_constructor(use_js=False)


    @allure.step('Перейти в раздел «Лента заказов»')
    def go_to_feed(self):
        self.open_page(Url.BASE_URL)
        self._click_outside_modal()
        super().go_to_order_feed(use_js=False)

    @allure.step('Открыть всплывающее окно ингредиента')
    def open_ingredient_modal(self):
        self.open_page(Url.BASE_URL)
        self.click_on_element(self.locators.FLUOR_BUN)
        self.wait_for_element_visible(self.locators.MODAL)

    @allure.step('Проверить, что всплывающее окно открыто')
    def modal_open(self):
        return self.element_displayed(self.locators.MODAL)

    @allure.step('Закрыть всплывающее окно по крестику')
    def close_ingredient_modal(self):
        self.click_on_element(self.locators.MODAL_CLOSE)
        self.wait_for_element_not_visible(self.locators.MODAL)

    @allure.step('Проверить, что всплывающее окно закрыто')
    def modal_closed(self):
        return self.element_hidden(self.locators.MODAL)

    @allure.step('Добавить булку в конструктор')
    def add_bun(self):
        self.drag_and_drop_ingredient(self.locators.INGREDIENT_BUN, self.locators.BURGER_CONSTRUCTOR)

    @allure.step('Добавить соус в конструктор')
    def add_sauce(self):
        self.drag_and_drop_ingredient(self.locators.INGREDIENT_SOUCE, self.locators.BURGER_CONSTRUCTOR)

    @allure.step('Получить счётчик соуса')
    def get_sauce_counter(self):
        return self.get_element_text(self.locators.INGREDIENT_COUNTER)
    