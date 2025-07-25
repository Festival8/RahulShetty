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
import random
import time

import pytest
from playwright.sync_api import Playwright, expect

from src.pageObject.login_page import LoginPage

with open('../data/user_creds.json') as creds_file:
    # load will convert json file into python object
    test_data = json.load(creds_file)
    user_creds_dict = test_data["user_creds"][0]

with open('../data/products.json') as products_file:
    products_data = json.load(products_file)
    products_list = products_data["products"]


@pytest.mark.parametrize("products", products_list)
def test_search_for_product(playwright: Playwright, browser_instance, products):
    # login
    email = user_creds_dict["email"]
    password = user_creds_dict["password"]
    login_page = LoginPage(browser_instance)
    dashboard_page = login_page.login(email=email, password=password)

    dashboard_page.verify_items_count(products_count=len(products_list))
    dashboard_page.verify_product_is_searchable(enter_data_for_search=products["name"])


def test_min_max_price(playwright: Playwright, browser_instance):
    # min price is fetched from first product
    # max price just price which is higher than min
    min_price = products_list[0]["price"]
    max_price = str(random.randint(int(products_list[0]["price"]), int(products_list[0]["price"]) + 500))

    # login
    email = user_creds_dict["email"]
    password = user_creds_dict["password"]
    login_page = LoginPage(browser_instance)
    dashboard_page = login_page.login(email=email, password=password)
    dashboard_page.verify_items_count(products_count=len(products_list))
    dashboard_page.set_up_min_max_value_in_products_filter(min_price=min_price, max_price=max_price)
    dashboard_page.verify_products_shown_in_range_selected_prices(min_price=min_price, max_price=max_price)
