from selenium import webdriver
import unittest
import HTMLTestRunner
class Asset(unittest.TestCase):
    def setUp(self): 
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.url = "http://10.22.2.26:4502"
        self.driver.get(self.url)
    def login(self):
        self.driver.find_element_by_id("username").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("admin")
        self.driver.find_element_by_tag_name("button").click()
        print "aem_asset ---------------------> login successfully"
        u'''Login'''
    def test_asset(self):
        self.login()
        self.driver.find_element_by_link_text("Assets").click()
        print "------------------> Test assets"
    def tearDown(self):
        self.driver.quit()
        print "------------------> close browser"
'''
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Asset("test_asset"))
    filename = r"C:\Users\shaopenggang\Desktop\selenium\test_result\result.html"
    fp = file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title="Report_title",
    description="Report_description")
    runner.run(suite)
   # unittest.main()
#test = testSign()
#test.login()

    results = unittest.TextTestRunner().run(suite)
'''