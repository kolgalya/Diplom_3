import allure
from pages.base_page import BasePage
from locators import MainPageLocators as MPL


class MainPage(BasePage):
    @allure.step('Клик по кнопке Личный кабинет')
    def click_personal_account(self):
        self.click_exit(MPL.PERSONAL_ACCOUNT)

    @allure.step('Клик по кнопке Личный кабинет')
    def click_personal(self):
        self.click(MPL.PERSONAL_ACCOUNT)

    @allure.step('Клик по кнопке Лента заказов')
    def click_order_feed(self):
        self.click_problem_element(MPL.ORDER_FEED)

    @allure.step('Клик по кнопке Лента заказов')
    def click_order_feed_after(self):
        self.click(MPL.ORDER_FEED)

    @allure.step('Получение текста заголовка конструктора')
    def get_text_construction(self):
        return self.get_text(MPL.CONSTRUCTION_TITLE)

    @allure.step('Клик по ингредиенту')
    def click_ingredient(self):
        self.click(MPL.FOUR_INGREDIENT)

    @allure.step('Получение текста заголовка окна с деталями ингредиента')
    def get_text_title_details_window(self):
        return self.get_text(MPL.TITLE_DETAILS_WINDOW)

    @allure.step('Клик по крестику окна с деталями ингредиента')
    def click_exit_details_window(self):
        self.click_exit(MPL.EXIT_DETAILS_WINDOW)

    @allure.step('Проверить наличие элемента на экране')
    def check_element(self):
        element = self.wait_element(MPL.TITLE_DETAILS_WINDOW)
        if element:
            return element.is_displayed()
        else:
            return False

    @allure.step('Скролл до ингредиента')
    def scroll_to_four_element(self):
        self.scroll_to_element(MPL.FOUR_INGREDIENT)

    @allure.step('Добавление булки в заказ')
    def add_to_the_order_buns(self):
        self.move_element(MPL.TWO_BUN, MPL.ORDER_SECTION)

    @allure.step('Добавление ингредиента в заказ')
    def add_to_the_order_ingredient(self):
        self.move_element(MPL.FOUR_INGREDIENT, MPL.ORDER_SECTION)

    @allure.step('Получить значение счетчика')
    def get_value_counter(self):
        return int(self.get_text(MPL.COUNTER_FOUR_INGREDIENT))

    @allure.step('Клик по кнопке Оформить заказ')
    def click_button_place_order(self):
        self.click(MPL.BUTTON_PLACE_ORDER)

    @allure.step('Ожидание загрузки главной страницы')
    def wait_element_main_page(self):
        return self.wait_element(MPL.ORDER_FEED)

    @allure.step('Получение номера заказа')
    def get_text_order_window(self):
        return self.get_text(MPL.INFO_WINDOW_ORDER)

    @allure.step('Ожидание загрузки номера заказа')
    def wait_text_number(self):
        self.wait_text(MPL.INFO_WINDOW_ORDER_NUMBER, '7')
        return self.get_text(MPL.INFO_WINDOW_ORDER_NUMBER)
