"""
test case: 1
1. search product
2. Add product to cart

test case: 2
1. set up min and max price product
2. Add product to cart

test case: 3
1. set up category
2. Add product to cart

test case: 4
1. set up category
2. Add product to cart

test case: 5
1. go to cart and check added products
2. Add product to card
"""
import json
import logging
import time

import pytest
from playwright.sync_api import Playwright, expect

from src.pageObject.login_page import LoginPage

with open('../data/user_creds.json') as creds_file:
    # load will convert json file into python onject
    test_data = json.load(creds_file)
    user_creds_dict = test_data["user_creds"][0]


@pytest.mark.parametrize("data", ["ZARA COAT 3", "ADIDAS ORIGINAL"])
def test_search_for_product(playwright: Playwright, browser_instance, data):
    # login
    email = user_creds_dict["email"]
    password = user_creds_dict["password"]

    login_page = LoginPage(browser_instance)
    dashboard_page = login_page.login(email=email, password=password)
    expect(browser_instance.locator('//div[@class="card-body"]/h5')).to_have_count(3)

    search_field = browser_instance.get_by_placeholder("search").nth(1)
    search_field.fill(data)
    search_field.press("Enter")
    time.sleep(2)

    cards = browser_instance.locator('//div[@class="card-body"]/h5')
    cards_count = cards.count()

    for i_card_num in range(cards_count):
        card = cards.nth(i_card_num)
        expect(card).to_contain_text(data)
