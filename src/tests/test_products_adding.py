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

from playwright.sync_api import Playwright

from src.pageObject.login_page import LoginPage

with open('../data/user_creds.json') as creds_file:
    # load will convert json file into python onject
    test_data = json.load(creds_file)
    user_creds_list = test_data["user_creds"]


def search_for_product_and_add_to_cart(playwright: Playwright, browser_instance):
    # login
    login_page = LoginPage(user_creds_list[browser_instance])
    login_page.login(email=user_creds_list[0]["email"], password=user_creds_list[0]["password"])

    #
