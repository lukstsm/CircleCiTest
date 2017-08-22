import os
from time import sleep

import unittest

from appium import webdriver
from base_test import BaseTest

# Returns abs path relative to this file and not cwd

class SimpleAndroidTests(BaseTest):
    def test_find_elements(self):
        el = self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "Text")]')
        return el.is_displayed()
