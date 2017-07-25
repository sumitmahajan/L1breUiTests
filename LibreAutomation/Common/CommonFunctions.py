import os
import unittest
from appium import webdriver
from time import sleep
import subprocess
from psutil import process_iter
from signal import SIGTERM

class Common(unittest.TestCase):

    process = ""

    def setUp(self):
        sleep(5)
        self.process = subprocess.Popen("appium --session-override", shell=True)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'W808'
        desired_caps['appPackage'] = 'com.tenone'
        desired_caps['appActivity'] = 'com.tenone.activity.SplashActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        sleep(5)
        self.driver.quit()
        self.process.kill()

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
        Common.clickOnId(self, "drivermode")
        Common.clickOnId(self, "button_no_pair")
        Common.enterTextOnId(self, "input_libre_id", userName)
        Common.enterTextOnId(self, "input_passwd", password)
        Common.clickOnId(self, "login_button")