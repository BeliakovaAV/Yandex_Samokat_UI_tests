from selenium.webdriver.common.by import By


class YesButtonPageLocator:
    YES_BUTTON = (By.XPATH, '//*[@id="root"]//button[text()="Да"]')