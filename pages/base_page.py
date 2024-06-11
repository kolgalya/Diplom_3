import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop
from selenium.webdriver import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Ожидание элемента и его выбор')
    def wait(self, locator):
        WDW(self.driver, 20).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидание наличия элемента на странице')
    def wait_element(self, locator):
        try:
            return WDW(self.driver, 20).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False

    @allure.step('Клик по элементу, который перекрыт другим')
    def click_problem_element(self, locator):
        filter_field = WDW(self.driver, 20).until(EC.element_to_be_clickable(locator))
        ActionChains(self.driver).move_to_element(filter_field).click().perform()

    @allure.step('Клик по крестику')
    def click_exit(self, locator):
        element = self.wait(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Клик по элементу')
    def click(self, locator):
        element = self.wait(locator)
        element.click()

    @allure.step('Получить текст')
    def get_text(self, locator):
        return self.wait(locator).text

    @allure.step('Получить класс')
    def get_class(self, locator):
        return self.wait(locator).get_attribute('class')

    @allure.step('Перетаскивание элемента')
    def move_element(self, locator_1, locator_2):
        element = self.wait(locator_1)
        target = self.wait(locator_2)
        drag_and_drop(self.driver, element, target)

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ввод текста')
    def add_text(self, locator, text):
        self.wait(locator).send_keys(text)

    @allure.step('Ожидание изменения текста')
    def wait_text(self, locator, text):
        WDW(self.driver, 20).until(EC.text_to_be_present_in_element(locator, text))
        return self.driver.find_element(*locator)
