from selenium import webdriver
import unittest
import aem_asset
class Site(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.url = "http://10.22.2.26:4502"
    def login(self):
        self.driver.get(self.url)
        self.driver.find_element_by_id("username").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("admin")
        self.driver.find_element_by_tag_name("button").click()
    def test_site(self):
        self.login()
        self.driver.find_element_by_link_text("Sites").click()
    def tearDown(self):
        self.driver.quit()
    
        
    