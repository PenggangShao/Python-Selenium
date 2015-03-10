from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import login
import time
class Classic(unittest.TestCase):
    def setUp(self):
        print "setup"
        self.driver = webdriver.Firefox()
        user_data = login.setdata()
        self.url = user_data[0]
        self.driver.implicitly_wait(3)
    def test_switch(self):
        driver = self.driver
        user_data = login.setdata()
        user_name = user_data[1]
        user_pass = user_data[2]
        driver.get(self.url)
        login.test_login(driver,user_name,user_pass)
        driver.find_element_by_link_text("Sites").click()
        WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_link_text("Sites"))
        ActionChains(driver).move_to_element(driver.find_element_by_link_text("Sites")).perform()
        ActionChains(driver).move_to_element(driver.find_element_by_xpath("html/body/div[2]/div[1]/div/nav[12]/a[3]/i")).perform()
        ActionChains(driver).click().perform()
        time.sleep(5)
        for handles in driver.window_handles:
            driver.switch_to_window(handles)
            print "-------------->",driver.title
            print "current tab",driver.title
        self.assertEqual("AEM WCM | Websites",self.driver.title)
        driver.find_element_by_id("extdd-18").click()
        print driver.title
        driver.find_element_by_id("extdd-48").click()
        driver.implicitly_wait(5)
        ActionChains(driver).move_to_element(driver.find_element_by_xpath(".//*[@id='cq-gen119']/div[1]/table/tbody/tr/td[3]/div")).perform()
        ActionChains(driver).context_click(driver.find_element_by_xpath(".//*[@id='cq-gen119']/div[1]/table/tbody/tr/td[3]/div")).perform()
        driver.implicitly_wait(3)
        driver.find_element_by_id("x-menu-el-ext-comp-1247").click()
        driver.implicitly_wait(3)
        driver.find_element_by_id('cq-gen359').click()
        driver.implicitly_wait(3)
        driver.find_element_by_id("ext-comp-1249__ext-comp-1286").click()
        driver.implicitly_wait(3)
        print driver.find_element_by_id("ext-comp-1249__ext-comp-1286").text
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