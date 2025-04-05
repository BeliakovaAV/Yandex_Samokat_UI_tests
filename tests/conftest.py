import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from url import *


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--width=1200")
    options.add_argument("--height=1080")
    driver = webdriver.Firefox(options=options)
    driver.get(main_site)

    yield driver
    driver.quit()