from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

@given(u'I launch chrome browser')
def step_impl(context):
    path = r"C:\Users\Bhushan\Desktop\driver files\chromedriver.exe"
    opt = webdriver.ChromeOptions()
    opt.add_argument("--disable-notifications")
    context.driver = webdriver.Chrome(executable_path=path)
    context.driver.maximize_window()
    context.driver.implicitly_wait(30)
    time.sleep(2)


@when(u'I Open Ajio homepage')
def step_impl(context):
    context.driver.get("https://www.ajio.com/")
    opt = webdriver.ChromeOptions()
    opt.add_argument("--disable-notifications")
    time.sleep(2)



@then(u'Click on Sign In button')
def step_impl(context):
    context.driver.find_element("xpath", "//span[text()='Sign In / Join AJIO']").click()
    time.sleep(2)


@then(u'Enter the mobile number')
def step_impl(context):
    context.driver.find_element("xpath", "//input[@name='username']").send_keys("9657212654")
    time.sleep(2)


@then(u'Click on continue button')
def step_impl(context):
    context.driver.find_element("xpath", "//input[@class='login-btn']").click()
    time.sleep(20)



@then(u'Click on start shopping button')
def step_impl(context):
    context.driver.find_element("xpath", "//input[@class='login-form-inputs login-btn']").click()
    time.sleep(5)



@then(u'search the product')
def step_impl(context):
    Search_ = context.driver.find_element("xpath",'//input[@class="react-autosuggest__input react-autosuggest__input--open"]')
    Search_.send_keys("kurthi")
    Search_.send_keys(Keys.ENTER)
    time.sleep(2)

@then(u'click on that product')
def step_impl(context):
    context.driver.find_element("xpath", "//div[@class='imgHolder']").click()
    handles = context.driver.window_handles
    context.driver.switch_to.window(context.driver.window_handles[1])
    time.sleep(3)


@then(u'select the size a')
def step_impl(context):
    context.driver.find_element("xpath", "//div[@class='circle size-variant-item size-instock ']").click()
    time.sleep(5)



@then(u'product add to wishlist')
def step_impl(context):
    context.driver.find_element("xpath", '(//span[@class="pdp-wishlist-desktop-icon"])[1]').click()
    handles = context.driver.window_handles
    context.driver.switch_to.window(context.driver.window_handles[1])
    time.sleep(5)


@then(u'click on wishlist to check wheather the product is added or not')
def step_impl(context):
    context.driver.find_element("xpath", '//img[@alt="wishlistIcon"]').click()
    time.sleep(2)


@then(u'go to back page c')
def step_impl(context):
    context.driver.back()


@then(u'remove from wishlist')
def step_impl(context):
    context.driver.find_element("xpath", "//span[@class='pdp-wishlist-desktop-icon']").click()
    time.sleep(2)



@then(u'click on wishlist to check wheather the product is removed or not')
def step_impl(context):
    context.driver.find_element("xpath", '//img[@alt="wishlistIcon"]').click()

@then(u'go to back page d')
def step_impl(context):
    context.driver.back()
    time.sleep(2)


@then(u'select the size b')
def step_impl(context):
    context.driver.find_element("xpath", "//div[@class='circle size-variant-item size-instock ']").click()
    time.sleep(2)


@then(u'product add to cart')
def step_impl(context):
    context.driver.find_element("xpath", "//div[@class='btn-gold']").click()
    time.sleep(3)


@then(u'click on cart')
def step_impl(context):
    context.driver.find_element("xpath", "//span[text()='GO TO BAG']").click()
    time.sleep(3)


@then(u'click on move to wishlist')
def step_impl(context):
    context.driver.find_element("xpath","//div[@class='save-closet-btn wishlist-icon-mr']").click()
    context.driver.back()


