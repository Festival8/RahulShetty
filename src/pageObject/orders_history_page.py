from playwright.sync_api import expect


class OrdersPage:
    def __init__(self, page):
        self.page = page

    def verify_order_message_when_order_open(self, order_id):
        orders = self.page.locator("tr").filter(has_text=order_id)
        orders.get_by_role("button", name="View").click()
        expect(self.page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")