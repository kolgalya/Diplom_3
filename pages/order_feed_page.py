import allure
from pages.base_page import BasePage
from locators import OrderFeedLocators as OFL

class OrderFeedPage(BasePage):
    @allure.step('Получаем текст заголовка Ленты заказов')
    def order_feed_title(self):
        return self.get_text(OFL.ORDER_FEED_TITLE)

    @allure.step('Клик на кнопку Конструктор')
    def click_button_construction(self):
        return self.click(OFL.BUTTON_CONSTRUCTION)

    @allure.step('Клик по 2-му заказу')
    def click_two_order(self):
        return self.click(OFL.TWO_ORDER)

    @allure.step('Получаем текст с всплывающего окна деталей заказа')
    def order_details(self):
        return self.get_text(OFL.ORDER_DETAILS_WINDOW)

    @allure.step('Скролл до заказа в Истории заказов')
    def scroll_to_order(self, number):
        self.scroll_to_element(OFL.ORDER_IN_HISTORY(number))

    @allure.step('Получаем текст последнего заказа')
    def get_text_last_order(self):
        return self.get_text(OFL.ORDER_IN_ORDER_FEED)

    @allure.step('Получаем значение счетчика Выполнено за все время')
    def get_text_сompleted_all_time(self):
        return self.get_text(OFL.COUNTER_COMPLET_ALL_TIME)

    @allure.step('Получаем значение счетчика Выполнено за сегодня')
    def get_text_сompleted_today(self):
        return self.get_text(OFL.COUNTER_COMPLET_TODAY)

    @allure.step('Получаем номер заказа в работе')
    def get_number_in_work(self):
        return self.get_text(OFL.NUMBER_IN_WORK)



