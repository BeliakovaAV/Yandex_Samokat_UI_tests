from selenium.webdriver.common.by import By


class MainPageLocators:
    UP_ORDER_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")
    DOWN_ORDER_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g Button_Middle__1CSJM")
    SAMOKAT_LOGO = (By.CSS_SELECTOR, 'img[src="/assets/scooter.svg"]')
    YANDEX_LOGO = (By.CSS_SELECTOR, 'img[src="/assets/ya.svg"]')

    @staticmethod
    def question_number(number):
        return By.ID, f'//*[@id="accordion__heading-{number}"]'