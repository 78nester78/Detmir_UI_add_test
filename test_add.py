
from card_product import AddToCart


def test_empty_cart(browser):
    empty_product_cart = AddToCart(browser)
    empty_product_cart.go_to_site()
    assert empty_product_cart.check_cart() == 'В корзину'


def test_add_to_cart(browser):
    card_product = AddToCart(browser)
    card_product.go_to_site()
    card_product.add_button()
    browser.refresh()
    assert card_product.check_cart() != 'В корзину'

