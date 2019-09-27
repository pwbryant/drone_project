import os
import unittest
from selenium import webdriver


class DroneTest(unittest.TestCase):

    def setUp(self):
        # self.browser = webdriver.Firefox()
        # self.browser = webdriver.Chrome()
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.browser = webdriver.Remote(
            command_executor='http://hub:4444/wd/hub',
            desired_capabilities=caps
        )

    def tearDown(self):
        self.browser.quit()

    def test_drone_in_title(self):
        browser = self.browser
        browser.get('http://web:8000')
        print('browser title', browser.title)
        self.assertIn('Drone', browser.title)
