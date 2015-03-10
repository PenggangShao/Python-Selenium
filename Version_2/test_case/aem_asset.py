from selenium import webdriver
import unittest
import os 
#import HTMLTestRunner
import login
class Asset(unittest.TestCase):
    print os.getcwd()
    def setUp(self): 
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        user_data = login.setdata()
        self.url = user_data[0]
        print self.url
    def test_asset(self):
        user_data = login.setdata()
        user_name = user_data[1]
        user_pass = user_data[2]
        driver = self.driver
        driver.get(self.url)
        login.test_login(driver,user_name,user_pass)
        driver.find_element_by_link_text(u"Assets").click()
    def tearDown(self):
        self.driver.quit()
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
    results = unittest.TextTestRunner().run(suite)
'''
