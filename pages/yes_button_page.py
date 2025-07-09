import allure
from pages.base_page import BasePage
from locators.yes_button_page_locator import YesButtonPageLocator


class YesButtonPage(BasePage):
    @allure.step("Кликнуть кнопку Да")
    def click_on_yes_button(self):
        self.click_on_element(YesButtonPageLocator.YES_BUTTON)
