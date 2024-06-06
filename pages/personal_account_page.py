import allure
from pages.base_page import BasePage
from locators import PersonalAccountLocators as PAL

class PersonalAccountPage(BasePage):
    @allure.step('Получаем класс кнопки Войти в Личном кабинете')
    def button_enter_class(self):
        return self.get_class(PAL.BUTTON_ENTER)

    @allure.step('Клик по кнопке Востановить пароль')
    def click_button_recover_password(self):
        return self.click(PAL.BUTTON_RECOVER_PASSWORD)

    @allure.step('Клик по кнопке История заказов')
    def click_button_order_history(self):
        return self.click(PAL.BUTTON_ORDER_HISTORY)

    @allure.step('Получить класс активной кнопки История заказов')
    def button_order_history_class(self):
        return self.get_class(PAL.BUTTON_ORDER_HISTORY)

    @allure.step('Ввести почту в окне авторизации')
    def add_mail(self, mail):
        self.add_text(PAL.FIELD_MAIL, mail)

    @allure.step('Ввести пароль в окне авторизации')
    def add_password(self, password):
        self.add_text(PAL.FIELD_PASSWORD, password)

    @allure.step('Клик по кнопке Войти')
    def click_button_enter(self):
        return self.click(PAL.BUTTON_ENTER)

    @allure.step('Клик по кнопке Выход')
    def click_exit(self):
        self.click(PAL.BUTTON_EXIT)

    @allure.step('Получение текста кнопки Войти')
    def get_text_enter(self):
        return self.get_text(PAL.BUTTON_ENTER)

    @allure.step('Получить номер последнего заказа')
    def get_text_last_order(self):
        return self.get_text(PAL.LAST_ORDER)

