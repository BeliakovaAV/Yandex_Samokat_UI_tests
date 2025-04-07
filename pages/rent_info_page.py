import allure
from data import *
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.rent_info_page_locators import RentInfoPageLocators


class RentInfoPage(BasePage):
    @allure.step("Выбрать дату доставки")
    def choose_arrival_date(self):
        self.click_on_element(RentInfoPageLocators.ARRIVAL_DATE)
        self.wait_for_element(RentInfoPageLocators.CHOOSE_DATE)
        self.click_on_element(RentInfoPageLocators.EXACT_DATE)

    @allure.step("Выбрать срок аренды")
    def choose_time_for_rent(self):
        self.click_on_element(RentInfoPageLocators.RENT_TIME)
        self.wait_for_element(RentInfoPageLocators.RENT_OPTION)
        self.click_on_element(RentInfoPageLocators.RENT_OPTION)

    @allure.step("Выбрать цвет самоката")
    def choose_color(self):
        self.click_on_element(RentInfoPageLocators.COLOR)

    @allure.step("Ввести данные в поле ввода Комментарий для курьера")
    def send_keys_to_input_comment(self, comment):
        self.click_on_element(RentInfoPageLocators.COMMENT)
        self.send_keys_to_input(RentInfoPageLocators.COMMENT, comment)

    @allure.step("Кликнуть на кнопку 'Заказать'")
    def click_on_order_button(self):
        self.click_on_element(RentInfoPageLocators.ORDER_BUTTON)