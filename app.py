from selenium import webdriver
#from selenium.webdriver.common.keys import keys

driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver')
driver.get("https://www.bestbuy.com/site/the-legend-of-zelda-skyward-sword-hd-nintendo-switch-lite-nintendo-switch/6414119.p?skuId=6414119")

addtocart = driver.find_element_by_class_name("btn-lg")

addtocart.click()

#gotocart = driver.find_element_by_class_name("c-button-secondary")

#refresh the page to get rid of the JS popup kekw
driver.refresh()

#cart is a link and not a button..
#maybe try getting a new page? does it retain that there is something in the cart?

cart = webdriver.Chrome('C:\chromedriver_win32\chromedriver')
cart.get("https://www.bestbuy.com/cart")
