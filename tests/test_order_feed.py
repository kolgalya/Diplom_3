import allure
from pages.main_page import MainPage as MP
from pages.order_feed_page import OrderFeedPage as OFP
from pages.personal_account_page import PersonalAccountPage as PAP
from data import Urls

class TestOrderPage:
    @allure.title('Клик по заказу открывает всплывающее окно с деталями заказа')
    def test_get_order_details(self, driver, create_user):
        user_data = create_user[1]
        main_page = MP(driver)
        main_page.open_page(Urls.url)
        main_page.click_personal_account()
        personal_account_page = PAP(driver)
        personal_account_page.add_mail(user_data["email"])
        personal_account_page.add_password(user_data["password"])
        personal_account_page.click_button_enter()
        main_page.click_order_feed_after()
        order_feed_page = OFP(driver)
        order_feed_page.click_two_order()
        assert 'Cостав' in order_feed_page.order_details()

    @allure.title('Заказ пользователя из раздела «История заказов» отображается на странице «Лента заказов»')
    def test_order_from_history_displayed_in_order_feed(self, driver, create_user):
        user_data = create_user[1]
        main_page = MP(driver)
        main_page.open_page(Urls.url)
        main_page.click_personal_account()
        personal_account_page = PAP(driver)
        personal_account_page.add_mail(user_data["email"])
        personal_account_page.add_password(user_data["password"])
        personal_account_page.click_button_enter()
        main_page.add_to_the_order_buns()
        main_page.add_to_the_order_ingredient()
        main_page.click_button_place_order()
        main_page.click_exit_details_window()
        main_page.click_personal_account()
        personal_account_page.click_button_order_history()
        order_number = personal_account_page.get_text_last_order()
        main_page.click_order_feed()
        order_feed_page = OFP(driver)
        assert order_number in order_feed_page.get_text_last_order()

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_counter_increased_completed_all_time(self, driver, create_user):
        user_data = create_user[1]
        main_page = MP(driver)
        main_page.open_page(Urls.url)
        main_page.click_personal_account()
        personal_account_page = PAP(driver)
        personal_account_page.add_mail(user_data["email"])
        personal_account_page.add_password(user_data["password"])
        personal_account_page.click_button_enter()
        main_page.click_order_feed_after()
        order_feed_page = OFP(driver)
        counter = int(order_feed_page.get_text_сompleted_all_time())
        order_feed_page.click_button_construction()
        main_page.add_to_the_order_buns()
        main_page.add_to_the_order_ingredient()
        main_page.click_button_place_order()
        main_page.click_exit_details_window()
        main_page.click_order_feed_after()
        counter_after = int(order_feed_page.get_text_сompleted_all_time())
        assert counter < counter_after

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_completed_today_counter_increasing(self, driver, create_user):
        user_data = create_user[1]
        main_page = MP(driver)
        main_page.open_page(Urls.url)
        main_page.click_personal_account()
        personal_account_page = PAP(driver)
        personal_account_page.add_mail(user_data["email"])
        personal_account_page.add_password(user_data["password"])
        personal_account_page.click_button_enter()
        main_page.wait_element_main_page()
        main_page.click_order_feed_after()
        order_feed_page = OFP(driver)
        counter = int(order_feed_page.get_text_сompleted_today())
        order_feed_page.click_button_construction()
        main_page.add_to_the_order_buns()
        main_page.add_to_the_order_ingredient()
        main_page.click_button_place_order()
        main_page.click_exit_details_window()
        main_page.click_order_feed_after()
        counter_after = int(order_feed_page.get_text_сompleted_today())
        assert counter < counter_after

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_order_number_in_progress_section(self, driver, create_user):
        user_data = create_user[1]
        main_page = MP(driver)
        main_page.open_page(Urls.url)
        main_page.click_personal_account()
        personal_account_page = PAP(driver)
        personal_account_page.add_mail(user_data["email"])
        personal_account_page.add_password(user_data["password"])
        personal_account_page.click_button_enter()
        main_page.add_to_the_order_buns()
        main_page.add_to_the_order_ingredient()
        main_page.click_button_place_order()
        number = main_page.wait_text_number()
        main_page.click_exit_details_window()
        main_page.click_order_feed()
        order_feed_page = OFP(driver)
        assert number in order_feed_page.get_number_in_work()
