import time
#class testcart
from selenium_mainassignment.pageobjects.cart import Cart
from selenium_mainassignment.utilities.BaseClass import BaseClass


class TestCart(BaseClass):

    def test_cart(self):
        #creating object for logging
        log = self.getlogger()

        #creating object of Cart class
        cart = Cart(self.driver)
        time.sleep(10)
        #select grocery
        cart.select_grocery()
        time.sleep(5)
        #Enter pincode
        cart.enter_pincode()
        time.sleep(10)
        #add items in cart
        cart.add_items_in_cart()
        time.sleep(5)
        #verify items in cart
        #cart.verify_items_in_cart()


