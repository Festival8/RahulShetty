from src.pageObject.dashboard_page import DashBoard


class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate_to_login_page(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def login(self, email, password):
        self.page.get_by_placeholder("email@example.com").fill(email)
        self.page.get_by_placeholder("enter your passsword").fill(password)
        self.page.get_by_role("button", name="Login").click()
        dashboard_page = DashBoard(self.page)
        return dashboard_page

