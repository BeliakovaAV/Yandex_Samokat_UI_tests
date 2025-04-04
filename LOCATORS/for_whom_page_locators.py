from selenium.webdriver.common.by import By


class ForWhomPageLocators:
    NAME = (By.XPATH, '//input[@placeholder="* Имя"]')
    SURNAME = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    #select.select_by_visible_text("Черкизовская")  # Выбрать по тексту
    PHONE = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    FURTHER_BUTTON = (By.XPATH, '//*[@id="root"]//button[text()="Далее"]')

