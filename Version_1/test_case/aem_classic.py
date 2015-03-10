from selenium import webdriver
from selenium.common.exceptions import  NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import HTMLTestRunner
import time
class Classic(unittest.TestCase):
    def setUp(self):
        print "setup"
        self.driver = webdriver.Firefox()
        self.url = "http://10.22.2.26:4502"
        self.driver.get(self.url)
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id("username").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("admin")
        self.driver.find_element_by_tag_name("button").click()
        self.driver.implicitly_wait(3)
    def test_switch(self):
        self.driver.find_element_by_link_text("Sites").click()
        WebDriverWait(self.driver,10).until(lambda driver:self.driver.find_element_by_link_text("Sites"))
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_link_text("Sites")).perform()
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("html/body/div[2]/div[1]/div/nav[12]/a[3]/i")).perform()
        ActionChains(self.driver).click().perform()
        time.sleep(5)
        for handles in self.driver.window_handles:
            self.driver.switch_to_window(handles)
            print "-------------->",self.driver.title
            print "current tab",self.driver.title
        self.assertEqual("AEM WCM | Websites",self.driver.title)
        self.driver.find_element_by_id("extdd-18").click()
        print self.driver.title
        self.driver.find_element_by_id("extdd-48").click()
        self.driver.implicitly_wait(5)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(".//*[@id='cq-gen119']/div[1]/table/tbody/tr/td[3]/div")).perform()
        ActionChains(self.driver).context_click(self.driver.find_element_by_xpath(".//*[@id='cq-gen119']/div[1]/table/tbody/tr/td[3]/div")).perform()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id("x-menu-el-ext-comp-1247").click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('cq-gen359').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id("ext-comp-1249__ext-comp-1286").click()
        self.driver.implicitly_wait(3)
        print self.driver.find_element_by_id("ext-comp-1249__ext-comp-1286").text
    def tearDown(self):
        self.driver.quit()
'''
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Classic("test_switch"))
    filename = r"C:\Users\shaopenggang\Desktop\selenium\test_result\result.html"
    fp = file(filename,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(
    stream = fp,
    description = "aem classic ui testing"
    )
    runner.run(suite)
'''