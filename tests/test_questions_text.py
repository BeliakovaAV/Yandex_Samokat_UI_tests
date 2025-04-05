import allure
import pytest

import data
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class TestQuestionsText:
    @allure.title("Тест текста вопросов")
    @pytest.mark.parametrize('question_text, expected_text', data.Data.questions)
    def test_questions_text(self, driver, question_text, expected_text):
        # Arrange
        main_page = MainPage(driver)
        main_page.scroll_for_questions_list()
        # Act
        main_page.click_on_question_arrow(question_text)
        main_page.wait_for_element(MainPageLocators.ANSWERS_IN_POPUP)
        # Assert
        assert main_page.check_question_text(expected_text)
