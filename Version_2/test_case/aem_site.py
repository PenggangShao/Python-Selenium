from selenium import webdriver
import unittest
import login
class Site(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        user_data = login.setdata()
        self.url = user_data[0]
    def test_site(self):
        user_data = login.setdata()
        user_name = user_data[1]
        user_pass = user_data[2]
        driver = self.driver
        driver.get(self.url)
        login.test_login(driver, user_name, user_pass)
        driver.find_element_by_link_text("Sites").click()
    def tearDown(self):
        self.driver.quit()
    
        
    