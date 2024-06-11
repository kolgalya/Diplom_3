import allure
from pages.main_page import MainPage as MP
from pages.personal_account_page import PersonalAccountPage as PAP
from data import Urls

class TestPersonalAccountPage:
    @allure.title('Клик по кнопке "История заказов" ведет в раздел история заказов')
    def test_click_order_history(self, driver, create_user):
        user_data = create_user[1]
        main_page = MP(driver)
        main_page.open_page(Urls.url)
        main_page.click_personal_account()
        personal_account_page = PAP(driver)
        personal_account_page.add_mail(user_data["email"])
        personal_account_page.add_password(user_data["password"])
        personal_account_page.click_button_enter()
        main_page.click_personal()
        personal_account_page.click_button_order_history()
        assert 'Account_link_active' in personal_account_page.button_order_history_class()

    @allure.title('Клик по кнопке "Выход"')
    def test_click_exit(self, driver, create_user):
        user_data = create_user[1]
        main_page = MP(driver)
        main_page.open_page(Urls.url)
        main_page.click_personal_account()
        personal_account_page = PAP(driver)
        personal_account_page.add_mail(user_data["email"])
        personal_account_page.add_password(user_data["password"])
        personal_account_page.click_button_enter()
        main_page.click_personal()
        personal_account_page.click_exit()
        assert 'Войти' in personal_account_page.get_text_enter()





