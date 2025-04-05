from selenium.webdriver.common.by import By


class MainPageLocators:
    UP_ORDER_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")
    DOWN_ORDER_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g Button_Middle__1CSJM")
    SAMOKAT_LOGO = (By.CSS_SELECTOR, 'img[src="/assets/scooter.svg"]')
    YANDEX_LOGO = (By.CSS_SELECTOR, 'img[src="/assets/ya.svg"]')
    QUESTIONS = (By.CLASS_NAME, "accordion__button")
    ANSWERS_IN_POPUP = (By.XPATH, '//div[contains(@class, "accordion__panel") and @id and contains(@id, "accordion__panel-")]//p')

    @staticmethod
    def question_text(question):
        return By.XPATH, f'//div[text()="{question}"]'
