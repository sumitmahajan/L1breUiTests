import socket
import subprocess
import unittest
from contextlib import closing
from time import sleep
import psutil
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
import pdb


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
            self.process = subprocess.Popen("appium --session-override", shell=True)
        desired_caps = {}
        desired_caps['newCommandTimeout'] = '999'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'W808'
        desired_caps['appPackage'] = 'com.tenone'
        desired_caps['appActivity'] = 'com.tenone.activity.SplashActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

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

    def swipe(self,id1,id2):
        self.driver.implicitly_wait(30)
        el1 = self.driver.find_element_by_id(id1)
        action = TouchAction(self.driver)
        el2 = self.driver.find_element_by_id(id2)
        action.long_press(el1).move_to(el2).release().perform()

    def setloc(self):
        self.driver.set_location(30.257364, -97.806956, 0.0)