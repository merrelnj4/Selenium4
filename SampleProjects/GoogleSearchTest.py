from selenium import webdriver
import unittest
import HTML-TestRunner

class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Albert/PycharmProjects/Selenium4/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_automation(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation")
        self.driver.find_element_by_name("btnK").click()
        print (self.driver.title)

    def test_search_raghav(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Raghav Pal")
        self.driver.find_element_by_name("btnK1").click()
        print (self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Albert/PycharmProjects/Selenium4/reports'))