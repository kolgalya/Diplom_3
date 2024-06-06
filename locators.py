from selenium.webdriver.common.by import By

class MainPageLocators():
    ORDER_FEED = (By.XPATH, "//p[contains(@class, 'AppHeader_header') and text() = 'Лента Заказов']")  # кнопка Лента заказoв
    PERSONAL_ACCOUNT = (By.LINK_TEXT, "Личный Кабинет") # кнопка Личный кабинет
    CONSTRUCTION_TITLE = (By.XPATH, "//main/section[contains(@class, 'BurgerIngredients')]/h1[text() = 'Соберите бургер']") #заголовок Соберите бургер
    FOUR_INGREDIENT = (By.XPATH, "//main/section[contains(@class, 'BurgerIngredients')]/div[2]/ul[2]/a[2]") # четвертый ингредиент в конструкторе - Соус фирменный Space Sauce
    COUNTER_FOUR_INGREDIENT = (By.XPATH, "//section[contains(@class,'BurgerIngredients')]/div[2]/ul[2]/a[2]/div[1]/p") # счетчик четвертого ингредиента в конструкторе
    TITLE_DETAILS_WINDOW = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//h2") # заголовок окна с деталями ингредиента
    EXIT_DETAILS_WINDOW = (By.XPATH, "//section[1]//button[contains(@class, 'Modal_modal__close')]")  # кнопка крестик окна с деталями ингредиента
    ORDER_SECTION = (By.XPATH, "//section[contains(@class, 'BurgerConstructor')]") # область сбора бургера (заказа)
    TWO_BUN = (By.XPATH, "//main/section[contains(@class, 'BurgerIngredients')]/div[2]/ul[1]/a[2]") # вторая булка в конструкторе - Краторная булка N-200i
    BUTTON_PLACE_ORDER = (By.XPATH, "//button[text() = 'Оформить заказ']") # кнопка Оформить заказ
    INFO_WINDOW_ORDER = (By.XPATH, "//p[text() = 'Ваш заказ начали готовить']")  # окно с деталями заказа
    INFO_WINDOW_ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow')]") # номер заказа в окне с деталями заказа

class PersonalAccountLocators():
    BUTTON_ENTER = (By.XPATH, "//button[text() = 'Войти']") # кнопка Войти в ЛК
    BUTTON_RECOVER_PASSWORD = (By.XPATH, "//a[text() = 'Восстановить пароль']") # кнопка Восcтановить пароль
    BUTTON_ORDER_HISTORY = (By.XPATH, "//a[text() = 'История заказов']")  # кнопка История заказов
    FIELD_MAIL = (By.XPATH, "//div[contains(@class, 'input')]/input[@name='name']")  # поле почта
    FIELD_PASSWORD = (By.XPATH, "//div[contains(@class, 'input')]/input[@name='Пароль']")  # поле пароль
    BUTTON_EXIT = (By.XPATH, "//button[text() = 'Выход']")  # кнопка выход
    LAST_ORDER = (By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList')]/li[last()]//div[contains(@class, 'OrderHistory_textBox')]/p[contains(@class, 'digits-default')]")  # номер последнего заказа в истории заказов

class PasswordRecoveryLocators():
    BUTTON_RECOVER = (By.XPATH, "//button[contains(@class, 'button_button')]")  # кнопка Восcтановить
    FIELD_MAIL_RECOVER_PASSWORD = (By.XPATH, "//div[contains(@class, 'input')]/input[@type='text']")  # поле Почта в окне Восcтановление пароля
    FIELD_PASSWORD_RECOVER_PASSWORD = (By.XPATH, "//label[contains(@class, 'input__placeholder') and text() = 'Пароль']")  # поле Пароль в окне Восcтановление пароля
    BUTTON_EYE = (By.XPATH, "//div[contains(@class, 'input__icon-action')]")  # кнопка глаз

class OrderFeedLocators():
    ORDER_FEED_TITLE = (By.XPATH, "//main/div[contains(@class, 'OrderFeed')]/h1[text() = 'Лента заказов']")
    BUTTON_CONSTRUCTION = (By.XPATH, "//p[contains(@class, 'AppHeader_header') and text() = 'Конструктор']")
    TWO_ORDER = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li[2]") # второй сверху заказ
    ORDER_DETAILS_WINDOW = (By.XPATH, "//p[text() = 'Cостав']") #окно деталей заказа
    ORDER_IN_ORDER_FEED = (By.XPATH, "//ul/li[1]//div[contains(@class, 'OrderHistory_textBox')]/p[1]") # номер заказа
    COUNTER_COMPLET_ALL_TIME = (By.XPATH, "//div[contains(@class, 'undefined')]/p[contains(@class, 'OrderFeed_number')]") # значение счетчика выполнено за все время
    COUNTER_COMPLET_TODAY = (By.XPATH, "//p[text() = 'Выполнено за сегодня:']/parent::div/p[2]") # значение счетчика выполнено за сегодня
    NUMBER_IN_WORK = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li[@class = 'text text_type_digits-default mb-2']") # номер заказа в разделе в работе