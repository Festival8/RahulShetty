import json

import pytest
from playwright.sync_api import Playwright, expect

from src.utils.api_base import APIUtils

with open('../data/user_creds.json') as creds_file:
    # load will convert json file into python onject
    test_data = json.load(creds_file)
    user_creds_list = test_data["user_creds"]

print(f"email: {user_creds_list[0]['email']}")


def test_just(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # create order
    api_util = APIUtils()
    order_id = api_util.create_oder(playwright, user_creds=user_creds_list[0])
    print(order_id)
