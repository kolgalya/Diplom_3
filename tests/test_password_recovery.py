import allure
import pytest
from data import Urls
from pages.main_page import MainPage as MP
from pages.personal_account_page import PersonalAccountPage as PAP
from pages.password_recovery_page import PasswordRecoveryPage as PRP

class TestPasswordRecovery:
    @allure.title('Клик по кнопке «Восстановить пароль» ведет на страницу восстановления пароля')
    def test_recover_password_true(self, driver):
        main_page = MP(driver)
        main_page.open_page(Urls.url)
        main_page.click_personal_account()
        personal_account_page = PAP(driver)
        personal_account_page.click_button_recover_password()
        password_recovery = PRP(driver)
        assert password_recovery.get_text_button_recover() == 'Восстановить'

    @pytest.mark.parametrize('mail', ['galya@yandex.ru', '', 2253, True])
    @allure.title('Ввод почты и клик по кнопке «Восстановить» ведет на страницу ввода нового пароля')
    def test_add_mail_click_button_recover_password_true(self, driver, mail):
        main_page = MP(driver)
        main_page.open_page(Urls.url)
        main_page.click_personal_account()
        personal_account_page = PAP(driver)
        personal_account_page.click_button_recover_password()
        password_recovery = PRP(driver)
        password_recovery.add_mail_recover_password(mail)
        password_recovery.click_button_recover()
        assert password_recovery.get_text_field_password() == 'Пароль'

    @allure.title('Клик по кнопке глаз делает поле Пароль активным')
    def test_click_button_eye_true(self, driver):
        main_page = MP(driver)
        main_page.open_page(Urls.url)
        main_page.click_personal_account()
        personal_account_page = PAP(driver)
        personal_account_page.click_button_recover_password()
        password_recovery = PRP(driver)
        password_recovery.add_mail_recover_password('galya@yandex.ru')
        password_recovery.click_button_recover()
        password_recovery.click_button_eye()
        assert 'input__placeholder-focused' in password_recovery.active_field_password_class()





