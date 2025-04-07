import allure
from pages.base_page import BasePage
from locators.confirmation_popup_locator import ConfirmationButtonPageLocator


class ConfirmationPopupPage(BasePage):
    @allure.step("Проверка появления окна с сообщением об успешном создании заказа")
    def confirmation_popup_check(self):
        try:
            self.wait_for_element(ConfirmationButtonPageLocator.CONFIRMATION_POPUP)
            return True
        except TimeoutException:
            return False
