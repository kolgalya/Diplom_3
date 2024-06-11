import allure
from pages.main_page import MainPage as MP
from pages.order_feed_page import OrderFeedPage as OFP
from pages.personal_account_page import PersonalAccountPage as PAP
from data import Urls

class TestMainPage:
    @allure.title('Клик по кнопке "Личный кабинет" ведет в личный кабинет')
    def test_click_personal_account(self, driver):
        main_page = MP(driver)
        main_page.open_page(Urls.url)
        main_page.click_personal_account()
        personal_account_page = PAP(driver)
        assert 'button_button' in personal_account_page.button_enter_class()

    @allure.title('Клик по "Лента заказов" ведет на страницу заказов')
    def test_click_order_feed(self, driver):
        main_page = MP(driver)
        main_page.open_page(Urls.url)
        main_page.click_order_feed()
        order_feed_page = OFP(driver)
        assert order_feed_page.order_feed_title() == 'Лента заказов'

    @allure.title('Клик по "Конструктор" ведет на страницу Соберите бургер')
    def test_click_construction(self, driver):
        main_page = MP(driver)
        main_page.open_page(Urls.url)
        main_page.click_order_feed()
        order_feed_page = OFP(driver)
        order_feed_page.click_button_construction()
        assert 'бургер' in main_page.get_text_construction()

    @allure.title('При клике по ингридиенту появляется всплывающее окно')
    def test_pop_up_window_ingredient(self, driver):
        main_page = MP(driver)
        main_page.open_page(Urls.url)
        main_page.click_ingredient()
        assert 'Детали' in main_page.get_text_title_details_window()

    @allure.title('При клике по крестику всплывающее окно закрывается')
    def test_close_window_ingredient(self, driver):
        main_page = MP(driver)
        main_page.open_page(Urls.url)
        main_page.click_ingredient()
        main_page.click_exit_details_window()
        assert main_page.check_element() == False

    @allure.title('При добавлении элемента в заказ его счетчик увеличивается')
    def test_add_ingredient(self, driver):
        main_page = MP(driver)
        main_page.open_page(Urls.url)
        main_page.scroll_to_four_element()
        counter_before = main_page.get_value_counter()
        main_page.add_to_the_order_ingredient()
        assert counter_before + 1 == main_page.get_value_counter()

    @allure.title('Авторизованный пользователь может оформить заказ')
    def test_place_order(self, driver, create_user):
        user_data = create_user[1]
        main_page = MP(driver)
        main_page.open_page(Urls.url)
        main_page.click_personal_account()
        personal_account_page = PAP(driver)
        personal_account_page.add_mail(user_data["email"])
        personal_account_page.add_password(user_data["password"])
        personal_account_page.click_button_enter()
        main_page.add_to_the_order_ingredient()
        main_page.click_button_place_order()
        assert 'Ваш заказ начали готовить' in main_page.get_text_order_window()
