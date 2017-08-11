import socket
import logging
import subprocess
import unittest
from contextlib import closing
from time import sleep
import psutil
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
import pdb
from selenium.common.exceptions import NoSuchElementException
from LibreAutomation.Common.Coords_Algorithm import Coords_Algorithm as ca

logging.basicConfig(filename=
                    "test.log"
                    , level=logging.INFO)

class CommonFunctions(unittest.TestCase):
    process = ""

    def check_socket(host, port):
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            if sock.connect_ex((host, port)) == 0:
                return True
            else:
                return False
    @staticmethod
    def setUpBase(self):
        chksession = CommonFunctions.check_socket("127.0.0.1",4723)
        if chksession == False:
            self.process = subprocess.Popen("appium -p 4723 -bp 4728 --chromedriver-port 9516 --session-override", shell=True)
        desired_caps = {}
        desired_caps['newCommandTimeout'] = '999'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'W808'
        desired_caps['appPackage'] = 'com.tenone'
        desired_caps['appActivity'] = 'com.tenone.activity.SplashActivity'
        desired_caps['autoAcceptAlerts'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    @staticmethod
    def setUpBaseParallel(self):
        chksession = CommonFunctions.check_socket("127.0.0.1",4723)
        if chksession == False:
            self.process = subprocess.Popen("appium -p 4725 -bp 4731 --chromedriver-port 9518 --session-override", shell=True)
        desired_caps = {}
        desired_caps['newCommandTimeout'] = '999'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = 'Users tablet2'
        desired_caps['appPackage'] = 'com.tenone'
        desired_caps['appActivity'] = 'com.tenone.activity.SplashActivity'
        desired_caps['autoAcceptAlerts'] = 'true'
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
        CommonFunctions.kill(self.process.pid)

    def clickOnId(self,id):
        self.driver.implicitly_wait(30)
        element = self.driver.find_element_by_id(id)
        element.click()


    def enterTextOnId(self,id,text):
        self.driver.implicitly_wait(30)
        element = self.driver.find_element_by_id(id)
        element.send_keys(text)

    def assertOnIdText(self,id,expValue):
        self.driver.implicitly_wait(30)
        element = self.driver.find_element_by_id(id)
        self.assertEqual(element.text, expValue)

    def loginDriver(self,userName,password):
        CommonFunctions.clickOnId(self, "drivermode")
        CommonFunctions.clickOnId(self, "button_no_pair")
        CommonFunctions.enterTextOnId(self, "input_libre_id", userName)
        CommonFunctions.enterTextOnId(self, "input_passwd", password)
        CommonFunctions.clickOnId(self, "login_button")
        CommonFunctions.bypass_wrong_password(self)

    def swipe(self,id1,id2):
        self.driver.implicitly_wait(30)
        el1 = self.driver.find_element_by_id(id1)
        action = TouchAction(self.driver)
        el2 = self.driver.find_element_by_id(id2)
        action.long_press(el1).move_to(el2).release().perform()

    def setloc(self):
        self.driver.set_location(19.426094, -99.163648, 0.0)
        sleep(5)

    def setincloc(self,n):
        self.driver.set_location(19.426094+n, -99.163648+n, 0.0)
        sleep(1)

    def bypass_wrong_password(self):
        if self.driver.find_elements_by_id("ok_button"):
            CommonFunctions.clickOnId(self, "ok_button")
            CommonFunctions.clickOnId(self, "login_button")


