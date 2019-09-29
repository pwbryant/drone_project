import os
from selenium import webdriver

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from hello.models import Greeting

class DroneTest(StaticLiveServerTestCase):

    host = 'web'
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        cls.browser = webdriver.Remote(
            command_executor='http://hub:4444/wd/hub',
            desired_capabilities=caps
        )

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_save_greetings(self):
        browser = self.browser
        browser.get(f'{self.live_server_url}/greetings/')

        sup = browser.find_element_by_tag_name('p').text
        self.assertEqual('sup?', sup)
        input_ = browser.find_element_by_id('id_greeting')
        input_.send_keys('Howdyz')
        submit = browser.find_elements_by_css_selector(
            'input[type="submit"]'
        )
        submit[0].click()
        new = browser.find_elements_by_tag_name('p')[-1].text
        self.assertEqual('Howdyz', new)

    def test_drone_in_title(self):
        browser = self.browser
        browser.get(self.live_server_url)
        self.assertIn('Drone', browser.title)
