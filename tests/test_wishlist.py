import time
from selenium_mainassignment.pageobjects.wishlist import WishList
from selenium_mainassignment.utilities.BaseClass import BaseClass



class TestWishList(BaseClass):

    def test_wishlist(self):
        #creating object of logging
        log = self.getlogger()
        #creating object of wishlist
        wishlist = WishList(self.driver)
        time.sleep(10)
        #calling function for searching fashion items
        wishlist.search_fashion_items()
        #calling function to add items in wishlist
        wishlist.add_items_to_wishlist()
        #calling function to verify items in wishlist
        wishlist.verify_items_in_wishlist()


