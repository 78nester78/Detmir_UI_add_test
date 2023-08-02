from selenium.webdriver.common.by import By
from base_page import BasePage


class Locators:
    ADD_TO_CART_BUTTON = (By.XPATH, '//*[@id="app-container"]/div[2]/main/div/div[1]/section[3]/section[1]/div[2]/div/div/div/button/span[4]')


class AddToCart(BasePage):

    def add_button(self):
        add_to_cart_button = self.find_element(Locators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()
        return add_to_cart_button

    def check_cart(self):
        check_cart = self.find_element(Locators.ADD_TO_CART_BUTTON)
        return check_cart.text
