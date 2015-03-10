from selenium import webdriver
def login():
    driver = webdriver.Firefox()
    driver.get("http://10.22.2.26:4502/")
    driver.implicitly_wait(5)
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_id("password").send_keys("admin")
    driver.find_element_by_tag_name("button").click()
   # driver.find_element_by_xpath(".//*[@id='cloudservicesprovisioning-wizard']/div[3]/button[1]").click()
#login()