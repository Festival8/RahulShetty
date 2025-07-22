from src.pageObject.orders_history_page import OrdersPage


class DashBoard:
    def __init__(self, page):
        self.page = page

    def navigate_to_orders_history(self):
        orders_button = self.page.get_by_role("button", name=" ORDERS")
        orders_button.click()
        orders_page = OrdersPage(self.page)
        return orders_page
