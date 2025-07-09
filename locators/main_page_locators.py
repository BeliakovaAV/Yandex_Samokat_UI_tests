from selenium.webdriver.common.by import By


class MainPageLocators:
    UP_ORDER_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")
    DOWN_ORDER_BUTTON = (By.CLASS_NAME, "Button_Middle__1CSJM")
    SAMOKAT_LOGO = (By.CSS_SELECTOR, 'img[src="/assets/scooter.svg"]')
    YANDEX_LOGO = (By.CSS_SELECTOR, 'img[src="/assets/ya.svg"]')
    QUESTIONS = (By.CLASS_NAME, "accordion__button")

    @staticmethod
    def question_text(question):
        return By.XPATH, f'//div[text()="{question}"]'

    @staticmethod
    def question_and_text(question_text):
        return By.XPATH, f"//div[@data-accordion-component='AccordionItem' and .//div[text()='{question_text}']]"

    @staticmethod
    def answer_inside_block():
        return By.XPATH, ".//div[@data-accordion-component='AccordionItemPanel']//p"
