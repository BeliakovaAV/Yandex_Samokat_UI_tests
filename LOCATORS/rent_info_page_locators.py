from selenium.webdriver.common.by import By


class RentInfoPageLocators:
    ARRIVAL_DATE = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    CHOOSE_DATE = (By.XPATH, '//*[@id="root"]//div[text()="30"]')
    RENT_TIME = (By.XPATH, '//*[@id="root"]//div[text()="* Срок аренды"]')
    #select.select_by_visible_text("сутки")  # Выбрать по тексту
    COLOR = (By.XPATH, '//*[@id="black"]')
    COMMENT = (By.XPATH, '//input[@placeholder="* Комментарий для курьера"]')
