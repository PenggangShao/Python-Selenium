from selenium import webdriver
import unittest
import HTMLTestRunner
from selenium.common.exceptions import NoSuchElementException
class Login(unittest.TestCase):
    def setUp(self): 
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.url = "http://10.22.2.26:4502"
   # @unittest.expectedFailure
    def test_login(self):
        u'''Login'''
        self.driver.get(self.url)
        self.driver.find_element_by_id("username").send_keys("admina")
        self.driver.find_element_by_id("password").send_keys("admin")
        self.driver.find_element_by_tag_name("button").click()
        self.driver.implicitly_wait(3)
        try:
            self.driver.find_element_by_xpath('//div[@class="endor-UserProfile-avatar endor-UserProfile-avatar--default"]').click()
            self.assertEqual("Administrator",self.driver.find_element_by_xpath('//span[@class="endor-Account-name"]').text)
        except NoSuchElementException:
            self.driver.get_screenshot_as_file(r"C:\Users\shaopenggang\Desktop\selenium\error\login.png")
            
        '''
        try:
            self.driver.find_element_by_xpath('//div[@class="endor-UserProfile-avatar endor-UserProfile-avatar--default"]').click()
            self.assertEqual("Administrator",self.driver.find_element_by_xpath('//span[@class="endor-Account-name"]').text)
        except:
            self.driver.get_screenshot_as_file(r"C:\Users\shaopenggang\Desktop\selenium\error\login.png")
    '''
    '''
    def test_asset(self):
        self.test_login()
        try:
            self.driver.find_element_by_link_text("A").click()
        except:
            self.driver.get_screenshot_as_file(r"C:\Users\shaopenggang\Desktop\selenium\error\asset.png")
    '''
    def tearDown(self):
        self.driver.quit()
        print "close browser!!!"
    '''
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Asset("test_login"))
    #suite.addTest(Asset("test_asset"))
  
    filename = r"C:\Users\shaopenggang\Desktop\selenium\test_result\result.html"
    fp = file(filename,"wb")
   # runner = unittest.TextTestRunner()
    runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title="result",
    description="Test Result"
    )
    runner.run(suite)
   # unittest.main()
#test = testSign()
#test.login()
 
    results = unittest.TextTestRunner().run(suite)
    '''