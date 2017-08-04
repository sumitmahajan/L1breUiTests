import unittest
import LibreAutomation.Common.CommonFunctions as cf
import pdb
from random import randint
from time import sleep


class TripSimulatorParallel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(TripSimulatorParallel, cls).setUpClass()
        cf.CommonFunctions.setUpBaseParallel(self=TripSimulatorParallel)

    def DriverLogin(self):
        cf.CommonFunctions.loginDriver(self," jgonzalez986","password")

    def DriverStartDay(self):
        cf.CommonFunctions.clickOnId(self,"driver_start")

    def DriverBooked(self):
        cf.CommonFunctions.clickOnId(self,"booked")

    def DriverStartTrip(self):
        cf.CommonFunctions.setloc(self)
        cf.CommonFunctions.swipe(self,"label_container","emergency_button_driver")
        cf.CommonFunctions.setloc(self)
        sleep(randint(1, 60))


    def DriverEndTrip(self):
        cf.CommonFunctions.swipe(self,"label_container","emergency_button_driver")

    def DriverFree(self):
        cf.CommonFunctions.clickOnId(self,"ratepaid")

    def DriverBreak(self):
        cf.CommonFunctions.clickOnId(self,"breakbutton")

    def DriverDisconnect(self):
        cf.CommonFunctions.clickOnId(self,"disconnect")

    def test_TripSimulator(self):
        TripSimulatorParallel.DriverLogin(self)
        TripSimulatorParallel.DriverStartDay(self)
        for i in range(200):
            TripSimulatorParallel.DriverBooked(self)
            TripSimulatorParallel.DriverStartTrip(self)
            TripSimulatorParallel.DriverEndTrip(self)
            TripSimulatorParallel.DriverFree(self)
        TripSimulatorParallel.DriverBreak(self)
        TripSimulatorParallel.DriverDisconnect(self)


    @classmethod
    def tearDownClass(cls):
        super(TripSimulatorParallel, cls).tearDownClass()
        cf.CommonFunctions.tearDownBase(self=TripSimulatorParallel)


#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TripSimulatorParallel)
    unittest.TextTestRunner(verbosity=2).run(suite)