import unittest
import LibreAutomation.Common.CommonFunctions as cf
import pdb


class DriverTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(DriverTests, cls).setUpClass()
        cf.CommonFunctions.setUpBase(self=DriverTests)

    def test_1DriverLogin(self):
        cf.CommonFunctions.loginDriver(self,"apacheco412","password")
        cf.CommonFunctions.assertOnIdText(self,"driver_name", "Alejandro B.")

    def test_2DriverStartDay(self):
        cf.CommonFunctions.clickOnId(self,"driver_start")

    def test_3DriverBooked(self):
        cf.CommonFunctions.clickOnId(self,"booked")

    def test_4DriverStartTrip(self):
        cf.CommonFunctions.swipe(self,"label_container","emergency_button_driver")

    def test_5DriverEndTrip(self):
        cf.CommonFunctions.swipe(self,"label_container","emergency_button_driver")

    def test_6DriverFree(self):
        cf.CommonFunctions.clickOnId(self,"ratepaid")

    def test_7DriverBreak(self):
        cf.CommonFunctions.clickOnId(self,"breakbutton")

    def test_8DriverDisconnect(self):
        cf.CommonFunctions.clickOnId(self,"disconnect")


    @classmethod
    def tearDownClass(cls):
        super(DriverTests, cls).tearDownClass()
        cf.CommonFunctions.tearDownBase(self=DriverTests)


#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DriverTests)
    unittest.TextTestRunner(verbosity=2).run(suite)