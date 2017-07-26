import unittest
import LibreAutomation.Common.CommonFunctions as cf


class DriverTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(DriverTests, cls).setUpClass()
        cf.CommonFunctions.setUpBase(self=DriverTests)

    def test_DriverLogin(self):
        cf.CommonFunctions.loginDriver(self,"apacheco412","password")
        cf.CommonFunctions.assertOnIdText(self,"driver_name", "Alejandro B.")

    def test_DriverStartDay(self):
        cf.CommonFunctions.clickOnId(self,"driver_start")


    @classmethod
    def tearDownClas(cls):
        super(DriverTests, cls).tearDownClass()
        cf.CommonFunctions.tearDownBase(self=DriverTests)


#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DriverTests)
    unittest.TextTestRunner(verbosity=2).run(suite)