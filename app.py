from selenium import webdriver
#from selenium.webdriver.common.keys import keys

driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver')
driver.get("https://www.bestbuy.com/site/the-legend-of-zelda-skyward-sword-hd-nintendo-switch-lite-nintendo-switch/6414119.p?skuId=6414119")

addtocart = driver.find_element_by_class_name("btn-lg")

addtocart.click()

#refresh the page to get rid of the JS popup kekw?it does still have the item in the cart
driver.refresh()

#click the go to cart link on the main product page
gotocart = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/header/div[1]/div/div[3]/div[1]/div/div/div/div/a')

gotocart.click()

checkout = driver.find_element_by_xpath('/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[3]/div/div[1]/button')

checkout.click()
