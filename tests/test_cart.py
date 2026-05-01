from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_add_to_cart(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    inventory.add_product()
    inventory.go_to_cart()
    
    product = cart.get_product_name()

    assert product == "Sauce Labs Backpack"





 