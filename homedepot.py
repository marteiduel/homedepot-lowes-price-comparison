from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

product_user = input("Enter the product you want to search: ")
# Path to your chromedriver executable
chrome_driver_path = 'C:/path/to/chromedriver.exe'

# Specify the path to your Chrome user profile
chrome_profile_path = 'C:/path/to/Chrome/Profile'

chrome_options = Options()
chrome_options.add_argument("user-data-dir=" + chrome_profile_path)

# Additional options if needed
chrome_options.add_argument("start-maximized")
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(
    executable_path=chrome_driver_path, options=chrome_options)

url = "https://www.homedepot.com/"

driver.get(url)

time.sleep(2)

search_bar_home_depot = driver.find_element(By.CLASS_NAME, "SearchBox__input")
search_bar_home_depot.send_keys(product_user)
search_button_home_depot = driver.find_element(
    By.CLASS_NAME, "SearchBox__button")
search_button_home_depot.click()

time.sleep(2.5)

results_home_depot = driver.find_elements(By.CLASS_NAME, "product-pod--ef6xv")

for result in results_home_depot:
    product_name = result.find_element(
        By.CLASS_NAME, "product-header__title-product--4y7oa").text
    product_brand = result.find_element(
        By.CLASS_NAME, "product-header__title__brand--bold--4y7oa").text
    # get price but remove first character which is a dollar sign and add a decimal point
    product_price = result.find_element(
        By.CLASS_NAME, "price-format__main-price").text
    price_length = len(product_price)
    price = product_price[0:price_length-2] + "." + \
        product_price[price_length-2:price_length]
    print(product_name)
    print(product_brand)
    print(price)
