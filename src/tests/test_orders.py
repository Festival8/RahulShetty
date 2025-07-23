import json

import pytest
from playwright.sync_api import Playwright, expect

from src.pageObject.dashboard_page import DashBoard
from src.pageObject.login_page import LoginPage
from src.utils.api_base import APIUtils

with open('../data/user_creds.json') as creds_file:
    # load will convert json file into python onject
    test_data = json.load(creds_file)
    user_creds_list = test_data["user_creds"]


@pytest.mark.parametrize("user_creds", user_creds_list)
def test_order_setup(playwright: Playwright, browser_instance, user_creds):
    # Create order using API
    api_util = APIUtils()
    order_id = api_util.create_oder(playwright, user_creds)

    # login
    login_page = LoginPage(browser_instance)
    dashboard_page = login_page.login(email=user_creds["email"], password=user_creds["password"])

    # Go to orders page and check if order is in the history
    ## NOTE: dashboard_page object is created in the login method,
    ## so that gives ability to call Dashboard class via login class
    order_history_page = dashboard_page.navigate_to_orders_history()
    order_history_page.verify_order_message_when_order_open(order_id=order_id)

