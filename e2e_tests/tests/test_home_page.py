import os
from splinter import Browser

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from hello.models import Greeting

class DroneTest(StaticLiveServerTestCase):

    host = 'web'
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        browser = Browser(
            driver_name="remote",
            url='http://hub:4444/wd/hub',
            browser=os.getenv('BROWSER', 'chrome'),
            name="Test of chrome"
        )
        cls.browser = browser

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_save_greetings(self):
        browser = self.browser
        browser.visit(f'{self.live_server_url}/greetings/')

        sup = browser.find_by_tag('p').text
        assert sup == 'sup?'
        input_ = browser.find_by_id('id_greeting')
        input_.fill('Howdyz')
        submit = browser.find_by_css(
            'input[type="submit"]'
        )
        submit[0].click()
        new = browser.find_by_tag('p').last.text
        assert new == 'Howdyz'

    def test_drone_in_title(self):
        browser = self.browser
        browser.visit(self.live_server_url)
        assert 'Drone' in browser.title