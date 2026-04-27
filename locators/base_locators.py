from selenium.webdriver.common.by import By


class BaseLocators:
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[contains(., 'Войти в аккаунт')]") # кнопка входа на главной
    EMAIL_FIELD = (By.XPATH, "//input[@type='text']") # поле email
    PASS_FIELD = (By.XPATH, "//input[@type='password']") # поле пароля
    LOGIN_BUTTON = (By.XPATH, "//button[contains(., 'Войти')]") # кнопка - Войти

    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']") # кнопка - Конструктор
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']") # кнопка - Лента заказов
    BURGER_CONSTRUCTOR = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list__l9dp_')]") # контейнер конструктора

    FLUOR_BUN = (By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]') # булка
    INGREDIENT_BUN = (By.XPATH, "//img[contains(@alt, 'Флюоресцентная булка R2-D3')]") # булка (ингредиент)
    INGREDIENT_SOUCE = (By.XPATH, "//img[contains(@alt, 'Соус Spicy-X')]") # соус (ингредиент)

    TITLE_FEED = (By.XPATH, "//h1[@class='text text_type_main-large mt-10 mb-5' and text()='Лента заказов']") # заголовок ленты

    INGREDIENT_COUNTER = (By.XPATH, "//p[text()='Соус Spicy-X']/ancestor::a//p[contains(@class, 'counter_counter__num')]") # счётчик соуса
    MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]") # всплывающее окно
    MODAL_CLOSE = (By.XPATH, '//button[contains(@class, "Modal_modal__close")]') # кнопка закрытия
    