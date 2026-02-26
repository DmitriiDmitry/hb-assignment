import os
from selenium import webdriver
import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL")


@pytest.fixture(scope="session")
def zip_code():
    return os.getenv("ZIP_CODE")


@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Chrome()
    yield browser

    browser.quit()