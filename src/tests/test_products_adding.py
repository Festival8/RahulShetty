"""
test case: 1
1. search product
DONE

test case: 2
1. set up min and max price product

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
import pytest
from playwright.sync_api import Playwright

from src.pageObject.login_page import LoginPage

with open('../data/user_creds.json') as creds_file:
    # load will convert json file into python onject
    test_data = json.load(creds_file)
    user_creds_dict = test_data["user_creds"][0]

with open('../data/products.json') as products_file:
    # load will convert json file into python onject
    products_data = json.load(products_file)
    products_dict = products_data["products"]


@pytest.mark.parametrize("data", products_dict)
def test_search_for_product(playwright: Playwright, browser_instance, data):
    # login
    email = user_creds_dict["email"]
    password = user_creds_dict["password"]

    login_page = LoginPage(browser_instance)
    dashboard_page = login_page.login(email=email, password=password)
    dashboard_page.verify_items_count(products_count=len(products_dict))
    dashboard_page.verify_product_is_searchable(enter_data_for_search=data)

