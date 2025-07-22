# all APIs methods will be created in the current class
from playwright.sync_api import Playwright

orders_payload = {"orders": [{"country": "India", "productOrderedId": "67a8dde5c0d3e6622a297cc8"}]}


class APIUtils:
    def get_token(self, playwright: Playwright, user_creds):
        email = user_creds["email"]
        password = user_creds["password"]
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post(url="/api/ecom/auth/login",
                                            data={"userEmail": email, "userPassword": password})
        return response.json()["token"]

    def create_oder(self, playwright: Playwright, user_creds):
        token = self.get_token(playwright, user_creds=user_creds)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post(url="/api/ecom/order/create-order",
                                            data=orders_payload,
                                            headers={"Authorization": token,
                                                     "Content-Type": "application/json"
                                                     })
        # this will retrieve json body
        print(f"Order creation response: {response.json()}")
        order_id = response.json()['orders'][0]
        return order_id

