import os
import unittest
from appium import webdriver
from time import sleep
import LibreAutomation.Common.CommonFunctions as cf

class DriverTests(unittest.TestCase):

    def setUp(self):
        cf.Common.setUp(self)

    def test_LibreLogin(self):
        cf.Common.loginDriver(self,"apacheco412","password")
        cf.Common.assertOnIdText(self,"driver_name", "Alejandro B.")

    def tearDown(self):
        cf.Common.tearDown(self)




#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DriverTests)
    unittest.TextTestRunner(verbosity=2).run(suite)