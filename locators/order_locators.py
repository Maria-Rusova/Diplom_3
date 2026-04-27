from selenium.webdriver.common.by import By
from locators.base_locators import BaseLocators


class OrderFeedLocators(BaseLocators):
    BUTTON_ORDER = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")  # кнопка - Оформить заказ
    ORDERS_IN_PROGRESS = (By.XPATH, "(//li[@class='text text_type_digits-default mb-2'])")  # номера заказов - В работе
    ID_ORDER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title__2L34m') and contains(@class, 'text_type_digits-large')]")  # номер заказа
    
    BUTTON_CLOSE_MODAL = (By.XPATH, '//button[contains(@class, "Modal_modal__close__TnseK")]')  # кнопка закрытия
    ORDER_OVERLAIN_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]")  # оверлей

    TOTAL_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p[contains(@class, 'text_type_digits-large')]")  # "выполнено за всё время"
    TODAY_ORDERS_COUNT = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p[contains(@class, 'text_type_digits-large')]")  # "выполнено за сегодня"
