import pytest
from selenium import webdriver
import os


@pytest.fixture
def driver():

    driver = webdriver.Chrome()

    path = os.path.abspath("app/index.html")
    driver.get("file://" + path)

    yield driver

    driver.quit()