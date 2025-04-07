import allure
from data import *

from pages.main_page import MainPage
from pages.rent_info_page import RentInfoPage
from pages.renter_info_page import RenterInfoPage
from pages.yes_button_page import YesButtonPage
from pages.confirmation_popup_page import ConfirmationPopupPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestOrder:
    @allure.title("Тест позитивного сценария заказа самоката (верхняя кнопка Заказать")
    def test_order_upper_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_up_order_button()
        renter_info_page = RenterInfoPage(driver)
        renter_info_page.send_keys_to_input_name(CredentialsFirstSet.name)
        renter_info_page.send_keys_to_input_surname(CredentialsFirstSet.surname)
        renter_info_page.send_keys_to_input_address(CredentialsFirstSet.address)
        renter_info_page.choose_metro(CredentialsFirstSet.metro)
        renter_info_page.send_keys_to_input_phone(CredentialsFirstSet.phone_number)
        renter_info_page.click_on_further_button()
        rent_info_page = RentInfoPage(driver)
        rent_info_page.choose_arrival_date()
        rent_info_page.choose_time_for_rent()
        rent_info_page.choose_color()
        rent_info_page.send_keys_to_input_comment(CredentialsFirstSet.comment)
        rent_info_page.click_on_order_button()
        yes_button_page = YesButtonPage(driver)
        yes_button_page.click_on_yes_button()
        confirmation_popup_page = ConfirmationPopupPage(driver)
        assert confirmation_popup_page.confirmation_popup_check()


