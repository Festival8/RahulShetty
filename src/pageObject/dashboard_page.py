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
