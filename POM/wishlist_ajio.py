from selenium.webdriver.common.keys import Keys
import time
from data_package import reading_objects
from data_package import reading_objects

locators = reading_objects.read_locators()

class Wishlist:
    def __init__(self,driver):
        self.driver = driver

    def sign_in(self):
        #sign_in
           self.driver.find_element(*locators["sign_in"]).click()
           time.sleep(2)

    def user_name(self):
        #user_name
        self.driver.find_element(*locators["user_name"]).send_keys("9657212654")
        time.sleep(2)

    def click_continue(self):
        #click_continue
        self.driver.find_element(*locators["click_continue"]).click()
        time.sleep(30)

    def start_shopping(self):
        #start_shopping
        self.driver.find_element(*locators["start_shopping"]).click()
        time.sleep(3)

    def search_products(self):
        #search_products`
        Search_ = self.driver.find_element(*locators["search_products"])
        Search_.send_keys("kurthi")
        Search_.send_keys(Keys.ENTER)
        time.sleep(3)

    def click_product(self):
        #clickproduct
        time.sleep(5)
        # self.driver.execute_script("window.scollBy(0,400)","")
        self.driver.find_element(*locators["click_product"]).click()
        time.sleep(3)

    def add_to_wishlist_b(self):
        #add_to_wishlist
        handles = self.driver.window_handles
        # driver.switch_to.window("https://www.ajio.com/anubhutee-indian-anarkali-kurta-set/p/463613694_blue")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element(*locators["add_to_wishlist_b"]).click()
        time.sleep(3)

        # self.driver.back()

    def click_on_wishlist_c(self):
        #click_on_wishlist
        self.driver.find_element(*locators["click_on_wishlist_c"]).click()
        time.sleep(2)
        self.driver.back()

    def remove_from_wishlist(self):
        #remove_from_wishlist
        self.driver.find_element(*locators["remove_from_wishlist"]).click()
        time.sleep(3)

    def click_on_wishlist_d(self):
        #click_on_wishlist_r
        self.driver.find_element(*locators["click_on_wishlist_d"]).click()
        time.sleep(3)
        self.driver.back()

    def select_size_e(self):
        # select_size
        self.driver.find_element(*locators["select_size_e"]).click()
        time.sleep(3)

    def add_to_cart(self):
        # add_to_cart
        self.driver.find_element(*locators["add_to_cart"]).click()
        time.sleep(3)

    def go_to_cart(self):
        # go_to_cart
        self.driver.find_element(*locators["go_to_cart"]).click()
        time.sleep(3)

    def move_to_wishlist(self):
        # add_to_wishlist
        self.driver.find_element(*locators["move_to_wishlist"]).click()
        time.sleep(3)
        self.driver.back()

    def remove_from_wishlist_b(self):
        self.driver.find_element(*locators["remove_from_wishlist_b"]).click()







