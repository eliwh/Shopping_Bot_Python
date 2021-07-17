from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver')
driver.get("https://www.bestbuy.com/site/the-legend-of-zelda-skyward-sword-hd-nintendo-switch-lite-nintendo-switch/6414119.p?skuId=6414119")

addtocart = driver.find_element_by_class_name("btn-lg")
addtocart.click()

#refresh the page to get rid of the JS popup kekw?it does still have the item in the cart
#driver.refresh()

#go to cart
driver.implicitly_wait(5)

gotocart = driver.find_element_by_xpath('/html/body/div[8]/div/div[1]/div/div/div/div/div[1]/div[3]/a')
gotocart.click()

#@ cart page
#select shipping
driver.implicitly_wait(5) # seconds

shipping = driver.find_element_by_xpath('/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[1]/div[4]/ul/li/section/div[2]/div[2]/form/div[2]/fieldset/div[2]/div[1]/div/div/div/input')
shipping.click()

driver.implicitly_wait(2) # seconds
checkout = driver.find_element_by_xpath('/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[3]/div/div[1]/button')
checkout.click()

#we are now at the signin page
driver.implicitly_wait(5) # seconds

email = driver.find_element_by_xpath("/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[1]/div/input")
password = driver.find_element_by_xpath("/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[2]/div/div/input")
email.send_keys("ehggghp@gmail.com")
password.send_keys("9SrPL3XZheiEGkC")

signin = driver.find_element_by_xpath("/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[3]/button")
signin.click()

#checkout page
driver.implicitly_wait(5)

#all the account details should be already input since they are saved
gotopayment = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button/span")
gotopayment.click()
