import logging.config
from os import path
import pytest
from playwright.sync_api import Playwright, expect

# Here the connection to the logs of our logging.ini file
log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.ini')
logging.config.fileConfig(log_file_path)


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption(
        "--url_name", action="store", default="https://rahulshettyacademy.com/client"
    )


@pytest.fixture
def browser_instance(playwright: Playwright, request):
    browser_name = request.config.getoption("browser_name")
    url_name = request.config.getoption("url_name")
    if browser_name == "chrome":
        browser_name = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser_name = playwright.firefox.launch(headless=False)

    context = browser_name.new_context()
    page = context.new_page()
    page.goto(url_name)
    yield page
    context.close()
    browser_name.close()
