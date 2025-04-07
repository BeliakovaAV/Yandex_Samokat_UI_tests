import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.renter_info_page_locators import RenterInfoPageLocators
from locators.main_page_locators import MainPageLocators


class RenterInfoPage(BasePage):

    @allure.step("Ввести текст в поле ввода Имя")
    def send_keys_to_input_name(self, name):
        self.click_on_element(RenterInfoPageLocators.NAME)
        self.send_keys_to_input(RenterInfoPageLocators.NAME, name)

    @allure.step("Ввести текст в поле ввода Фамилия")
    def send_keys_to_input_surname(self, surname):
        self.click_on_element(RenterInfoPageLocators.SURNAME)
        self.send_keys_to_input(RenterInfoPageLocators.SURNAME, surname)

    @allure.step("Ввести текст в поле ввода Адрес")
    def send_keys_to_input_address(self, address):
        self.click_on_element(RenterInfoPageLocators.ADDRESS)
        self.send_keys_to_input(RenterInfoPageLocators.ADDRESS, address)

    @allure.step("Выбрать станцию метро")
    def choose_metro(self, metro):
        self.send_keys_to_input(RenterInfoPageLocators.METRO, metro)
        element = self.driver.find_element(*RenterInfoPageLocators.METRO)
        element.send_keys(Keys.ARROW_DOWN)
        element.send_keys(Keys.ENTER)

    @allure.step("Ввести цифры в поле ввода Телефон")
    def send_keys_to_input_phone(self, phone):
        self.click_on_element(RenterInfoPageLocators.PHONE)
        self.send_keys_to_input(RenterInfoPageLocators.PHONE, phone)

    @allure.step("Кликнуть на кнопку Далее")
    def click_on_further_button(self):
        self.click_on_element(RenterInfoPageLocators.FURTHER_BUTTON)
