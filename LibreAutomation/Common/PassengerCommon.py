import unittest
import subprocess
import psutil
from time import sleep
from appium import webdriver

class PassengerCommon(unittest.TestCase):
    @staticmethod
    def setUpBase(self):
        self.process = subprocess.Popen("appium -p 4725 --session-override", shell=True)
        desired_caps = {}
        desired_caps['newCommandTimeout'] = '999'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'W101'
        desired_caps['appPackage'] = 'com.tenone'
        desired_caps['appActivity'] = 'com.tenone.activity.SplashActivity'
        self.driver = webdriver.Remote('http://localhost:4725/wd/hub', desired_caps)

    def kill(proc_pid):
        process = psutil.Process(proc_pid)
        for proc in process.children(recursive=True):
            proc.kill()
        process.kill()


    @staticmethod
    def tearDownBase(self):
        sleep(5)
        self.driver.quit()
        PassengerCommon.kill(self.process.pid)


    def test_1(self0):
        PassengerCommon.setUpBase(self=webdriver)

        PassengerCommon.tearDownBase(self=webdriver)

#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PassengerCommon)
    unittest.TextTestRunner(verbosity=2).run(suite)