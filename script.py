from library.basic_selenium_actions import *
from Constants.xpaths.saucedemo_login import *
from Constants.xpaths.saucedemo_inventory import *
from Constants.xpaths.items_description import *
from Constants.xpaths.saucedemo_your_info import *
import time

web_url = "https://www.saucedemo.com/"
driver = open_browser_to_link(web_url)
time.sleep(3)
enter_text_in_element(driver, txt_box_username, "standard_user")
enter_text_in_element(driver, txt_box_password, "secret_sauce")
click_element(driver, btn_login)
time.sleep(1)
select_value_in_dropdown(driver, dropdown_sort, "lohi")
time.sleep(1)

item1 = get_element_text(driver, bike_light)
print("I am going to buy: ", item1)
click_element(driver, bike_light)
time.sleep(1)
click_element(driver, btn_add_to_cart)
time.sleep(1)
click_element(driver, btn_back_to_products)
time.sleep(1)
select_value_in_dropdown(driver, dropdown_sort, "lohi")
scroll_to_element(driver, fleece_jacket)
time.sleep(1)

item2 = get_element_text(driver, fleece_jacket)
print("I am going to buy: ", item2)
time.sleep(1)
click_element(driver, fleece_jacket)
time.sleep(1)
click_element(driver, btn_add_to_cart)
time.sleep(1)
click_element(driver, btn_back_to_products)
time.sleep(2)

item3 = get_element_text(driver, labs_backpack)
print("I am going to buy: ", item3)
click_element(driver, labs_backpack)
time.sleep(1)
click_element(driver, btn_add_to_cart)
time.sleep(10)

click_element(driver, shopping_cart)
time.sleep(10)

scroll_to_element(driver, labs_backpack)
time.sleep(10)

click_element(driver, btn_checkout)
time.sleep(10)

enter_text_in_element(driver, txt_first_name, "saloni")
time.sleep(3)
enter_text_in_element(driver, txt_last_name, "B")
time.sleep(3)
enter_text_in_element(driver, txt_zip_code, "454357")
time.sleep(3)
click_element(driver, btn_continue)
time.sleep(10)

finish = click_element(driver, btn_finish)
print(" Thank you for your order! ", finish)
time.sleep(10)
