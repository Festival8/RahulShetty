import logging
import time

from playwright.sync_api import expect

from src.pageObject.orders_history_page import OrdersPage


class DashBoard:
    def __init__(self, page):
        self.page = page

    def navigate_to_orders_history(self):
        orders_button = self.page.get_by_role("button", name=" ORDERS")
        orders_button.click()
        orders_page = OrdersPage(self.page)
        return orders_page

    def verify_items_count(self, products_count: int):
        expect(self.page.locator('//div[@class="card-body"]/h5')).to_have_count(products_count)

    def verify_product_is_searchable(self, enter_data_for_search: str):
        search_field = self.page.get_by_placeholder("search").nth(1)
        search_field.fill(enter_data_for_search)
        search_field.press("Enter")
        time.sleep(2)

        cards = self.page.locator('//div[@class="card-body"]/h5')
        cards_count = cards.count()

        for i_card_num in range(cards_count):
            card = cards.nth(i_card_num)
            expect(card).to_contain_text(enter_data_for_search)

    def set_up_min_max_value_in_products_filter(self, min_price, max_price):
        min_field = self.page.get_by_placeholder("Min Price").nth(1)
        max_field = self.page.get_by_placeholder("Max Price").nth(1)

        min_field.fill(min_price)
        max_field.fill(max_price)
        self.page.locator("//div[@id='res']").click()

    def verify_products_shown_in_range_selected_prices(self, min_price, max_price):
        time.sleep(2)
        card_body_list = self.page.locator(".card").all()

        for i_card in card_body_list:
            card_price = i_card.locator("div > div").nth(0)
            price = int(card_price.inner_text().split()[1])
            print(f"LOGS: Price: {price} Range: {int(min_price), int(max_price)}")
            assert price in range(int(min_price), int(max_price))
