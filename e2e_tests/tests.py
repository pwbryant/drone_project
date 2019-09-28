import os
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class DroneTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):

        cls.host = 'web'
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        cls.browser = webdriver.Remote(
            command_executor='http://hub:4444/wd/hub',
            desired_capabilities=caps
        )
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def test_drone_in_title(self):
        browser = self.browser
        browser.get(self.live_server_url)
        self.assertIn('Drone', browser.title)
