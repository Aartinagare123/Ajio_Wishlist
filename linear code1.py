
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
file_path=r"C:\Users\Bhushan\Downloads\chromedriver_win32\chromedriver.exe"

opt=webdriver.ChromeOptions()

opt.add_argument("--disable-notifications")
driver=webdriver.Chrome(executable_path=file_path,options=opt)
driver.implicitly_wait(50)
driver.get('https://www.ajio.com/')
driver.maximize_window()

# sign_in
driver.find_element("xpath","//span[text()='Sign In / Join AJIO']").click()

# user_name
driver.find_element("xpath","//input[@name='username']").send_keys("9657212654")

# click_continue
driver.find_element("xpath","//input[@class='login-btn']").click()
time.sleep(30)

#start_shopping
driver.find_element("xpath","//input[@class='login-form-inputs login-btn']").click()

# search_product
Search_ = driver.find_element("xpath",'//input[@class="react-autosuggest__input react-autosuggest__input--open"]')
Search_.send_keys("kurthi")
Search_.send_keys(Keys.ENTER)

#click_product
driver.find_element("xpath","//div[@class='imgHolder']").click()
handles = driver.window_handles
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)

# select_size_a
# i = [S,M,L,XL,XXL]
# buttons = driver.find_elements("xpath","//div[@class='size-variant-block']/..//div[@class='size-swatch']").click()
# print(len(buttons))
# for item in i:
#     driver
#     break
driver.find_element("xpath","//div[@class='circle size-variant-item size-instock ']").click()
time.sleep(2)

# add_to_wishlist
driver.find_element("xpath",'(//span[@class="pdp-wishlist-desktop-icon"])[1]').click()
time.sleep(2)
# driver.back()

# click_on_wishlist_a
driver.find_element("xpath",'//img[@alt="wishlistIcon"]').click()
driver.back()
time.sleep(3)

# remove_from_wishlist
driver.find_element("xpath","//span[@class='pdp-wishlist-desktop-icon']").click()
time.sleep(3)

# click_on_wishlist_r
driver.find_element("xpath",'//img[@alt="wishlistIcon"]').click()
driver.back()
time.sleep(3)

# select_size1
driver.find_element("xpath","//div[@class='circle size-variant-item size-instock ']").click()
time.sleep(3)

# add_to_cart
driver.find_element("xpath","//div[@class='btn-gold']").click()
time.sleep(3)

# go_to_bag
driver.find_element("xpath","//span[text()='GO TO BAG']").click()
time.sleep(3)

# move_to_wishlist
driver.find_element("xpath","//div[@class='save-closet-btn wishlist-icon-mr']").click()
time.sleep(3)
driver.close()




