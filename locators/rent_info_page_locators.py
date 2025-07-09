from selenium.webdriver.common.by import By


class RentInfoPageLocators:
    ARRIVAL_DATE = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    CHOOSE_DATE = (By.CLASS_NAME, "react-datepicker__month-container")
    EXACT_DATE = (By.XPATH, "//div[text()='9']")
    RENT_TIME = (By.XPATH, '//*[@id="root"]//div[text()="* Срок аренды"]')
    RENT_OPTION = (By.XPATH, "//div[@class='Dropdown-option' and text()='четверо суток']")
    COLOR = (By.XPATH, '//*[@id="black"]')
    COMMENT = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Middle__1CSJM") and text()="Заказать"]')


