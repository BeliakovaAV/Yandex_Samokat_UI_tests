import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Кликнуть на кнопку 'Заказать' в верхней части страницы ")
    def click_on_up_order_button(self):
        self.click_on_element(MainPageLocators.UP_ORDER_BUTTON)

    @allure.step("Кликнуть на кнопку 'Заказать' в нижней части страницы ")
    def click_on_down_order_button(self):
        self.scroll_to_element(MainPageLocators.DOWN_ORDER_BUTTON)
        self.click_on_element(MainPageLocators.DOWN_ORDER_BUTTON)

    @allure.step("Проскроллить до списка вопросов")
    def scroll_for_questions_list(self):
        self.scroll_to_element(MainPageLocators.QUESTIONS)

    @allure.step("Кликнуть на стрелочку с вопросом")
    def click_on_question_arrow(self, question_text):
        question_locator = MainPageLocators.question_text(question_text)
        self.click_on_element(question_locator)

    @allure.step("Сравнить текст вопроса")
    def check_question_text(self, question_text, expected_text):
        locator = MainPageLocators.question_and_text(question_text)
        full_block = self.wait_for_element(locator)
        answer_locator = MainPageLocators.answer_inside_block()
        answer = full_block.find_element(*answer_locator)
        actual_text = answer.text.strip()
        return expected_text == actual_text

    @allure.step("Нажать на лого Самокат")
    def click_on_samokat(self):
        self.click_on_element(MainPageLocators.SAMOKAT_LOGO)

    @allure.step("Нажать на лого Яндекс")
    def click_on_yandex(self):
        self.click_on_element(MainPageLocators.YANDEX_LOGO)
