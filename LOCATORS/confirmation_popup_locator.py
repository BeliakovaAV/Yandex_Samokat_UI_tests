from selenium.webdriver.common.by import By


class ConfirmationButtonPageLocator:
    CONFIRMATION_POPUP = (By.XPATH, '//div[text()="Заказ оформлен"]')