"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.

from django.test.testcases import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
import os
os.environ['DISPLAY'] = ':1'
class SeleniumTestCases(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(SeleniumTestCases, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(SeleniumTestCases, cls).tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, 'accounts/login/'))
        username_input = self.selenium.find_element_by_name("id_username")
        username_input.send_keys('myuser')
        password_input = self.selenium.find_element_by_name("id_password")
        password_input.send_keys('secret')
        self.selenium.find_element_by_xpath('//input[@value="Sign in"]').click()

        WebDriverWait(self.selenium, timeout).until(
        lambda driver: driver.find_element_by_tag_name('body'))
"""
