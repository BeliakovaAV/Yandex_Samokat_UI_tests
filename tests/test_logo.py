import allure
from selenium.webdriver.support.ui import WebDriverWait

from pages.main_page import MainPage
from url import *


class TestLogo:
    @allure.title("Тест перехода по клику на лого Самокат")
    def test_click_on_samokat(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_up_order_button()
        main_page.click_on_samokat()
        current_url = main_page.driver.current_url
        assert current_url == main_site


    @allure.title("Тест перехода по клику на лого Яндекс")
    def test_click_on_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_yandex()
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 20).until(lambda d: d.execute_script("return document.readyState") == "complete")
        current_url = main_page.driver.current_url
        assert current_url == dzen_page
