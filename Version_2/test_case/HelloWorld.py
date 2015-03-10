import login
from selenium import webdriver
import time
user_data = login.setdata()
url = user_data[0]
user_name = user_data[1]
user_pass = user_data[2]
print url[0]
driver = webdriver.Firefox()
driver.get(url)
login.test_login(driver,user_name,user_pass)
time.sleep(3)
driver.close()
driver.quit()