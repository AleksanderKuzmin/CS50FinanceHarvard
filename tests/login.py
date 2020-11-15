import unittest
from time import sleep
from selenium import webdriver


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='../browser_drivers/geckodriver')
        self.browser.get('http://127.0.0.1:5000/login')
        self.addCleanup(self.browser.quit)

    def test_login_page_exist(self):
        browser = self.browser
        sleep(4)
        login_text = browser.find_element_by_xpath('//*[@id="navbar"]/ul/li[2]/a').text
        self.assertEqual('Log In', login_text)


if __name__ == '__main__':
    unittest.main()
