import allure
from pages.base_page import BasePage
from locators import PasswordRecoveryLocators as PRL

class PasswordRecoveryPage(BasePage):
    @allure.step('Получить номер последнего заказа')
    def get_text_last_order(self):
       return self.get_text(PRL.LAST_ORDER)

    @allure.step('Получаем текст на кнопке Востановить')
    def get_text_button_recover(self):
        return self.get_text(PRL.BUTTON_RECOVER)

    @allure.step('Ввести почту в окне востановления пароля')
    def add_mail_recover_password(self, mail):
        self.add_text(PRL.FIELD_MAIL_RECOVER_PASSWORD, mail)

    @allure.step('Клик по кнопке Востановить')
    def click_button_recover(self):
        return self.click(PRL.BUTTON_RECOVER)

    @allure.step('Получаем текст в поле Пароль в окне востановления пароля')
    def get_text_field_password(self):
        return self.get_text(PRL.FIELD_PASSWORD_RECOVER_PASSWORD)

    @allure.step('Клик по кнопке глаз')
    def click_button_eye(self):
        return self.click(PRL.BUTTON_EYE)

    @allure.step('Получаем класс активного поля ввода пароля')
    def active_field_password_class(self):
        return self.get_class(PRL.FIELD_PASSWORD_RECOVER_PASSWORD)








