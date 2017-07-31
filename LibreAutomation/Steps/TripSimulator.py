import unittest
import LibreAutomation.Common.CommonFunctions as cf
import pdb
from random import randint
from time import sleep


class TripSimulator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(TripSimulator, cls).setUpClass()
        cf.CommonFunctions.setUpBase(self=TripSimulator)

    def DriverLogin(self):
        cf.CommonFunctions.loginDriver(self,"rjimenez895","Oracle123")

    def DriverStartDay(self):
        cf.CommonFunctions.clickOnId(self,"driver_start")

    def DriverBooked(self):
        cf.CommonFunctions.clickOnId(self,"booked")

    def DriverStartTrip(self):
        cf.CommonFunctions.swipe(self,"label_container","emergency_button_driver")
        cf.CommonFunctions.setloc(self)
        sleep(randint(1, 300))


    def DriverEndTrip(self):
        cf.CommonFunctions.swipe(self,"label_container","emergency_button_driver")

    def DriverFree(self):
        cf.CommonFunctions.clickOnId(self,"ratepaid")

    def DriverBreak(self):
        cf.CommonFunctions.clickOnId(self,"breakbutton")

    def DriverDisconnect(self):
        cf.CommonFunctions.clickOnId(self,"disconnect")

    def test_TripSimulator(self):
        TripSimulator.DriverLogin(self)
        TripSimulator.DriverStartDay(self)
        for i in range(20):
            TripSimulator.DriverBooked(self)
            TripSimulator.DriverStartTrip(self)
            TripSimulator.DriverEndTrip(self)
            TripSimulator.DriverFree(self)
        TripSimulator.DriverBreak(self)
        TripSimulator.DriverDisconnect(self)


    @classmethod
    def tearDownClass(cls):
        super(TripSimulator, cls).tearDownClass()
        cf.CommonFunctions.tearDownBase(self=TripSimulator)


#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TripSimulator)
    unittest.TextTestRunner(verbosity=2).run(suite)