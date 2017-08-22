import unittest
from appium import webdriver

class BaseTest(unittest.TestCase):
    """Basis for all tests."""
    def setUp(self):
        """Sets up desired capabilities and the Appium driver."""
        url = 'http://127.0.0.1:4723/wd/hub'
        desired_caps = {}

        """
        The following desired capabilities must be set when running locally.
        Make sure they are NOT set when uploading to Device Farm.
        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
        )
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'FA7520302898'
        desired_caps['app'] = PATH('../mobile-debug.apk')
        """
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'aPhone'
        self.driver = webdriver.Remote(url, desired_caps)

    def tearDown(self):
        """Shuts down the driver."""
        self.driver.quit()

    def get_name(self):
        raise NotImplementedError
