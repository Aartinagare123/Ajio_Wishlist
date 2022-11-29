

from POM.wishlist_ajio import Wishlist

class TestWishlist:
    def test_wishlist(self,_driver):
        obj = Wishlist(_driver)
        _driver.implicitly_wait(30)
        obj.sign_in()
        obj.user_name()
        obj.click_continue()
        obj.start_shopping()
        obj.search_products()
        obj.click_product()
        obj.add_to_wishlist_b()
        obj.click_on_wishlist_c()
        obj.remove_from_wishlist()
        obj.click_on_wishlist_d()
        obj.select_size_e()
        obj.add_to_cart()
        obj.go_to_cart()
        obj.move_to_wishlist()
        obj.remove_from_wishlist_b()