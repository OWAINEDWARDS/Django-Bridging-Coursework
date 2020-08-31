from selenium import webdriver
from django.test import TestCase
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox();

    def tearDown(self):
        self.browser.quit()

    def test_homepage_view(self):
        self.browser.get("http://localhost:8000")
        self.assertIn('Home', self.browser.title)
        begin_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Owain Edwards', begin_text)

        # self.fail('finish the test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
