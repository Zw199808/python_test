import sys
sys.path.append('../page')
sys.path.append('../basePage')
from basePage.homeBase import *
from page.loginpage import *
from selenium import webdriver
import unittest
import time


class MyUnitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.url = 'https://nku.xiaokesi.com/system/user/login'
        self.driver.implicitly_wait(10)
        # 实例化一个loginpage对象

        self.loginPage = LoginPage(self.url, self.driver)

    def tearDown(self) -> None:
        self.driver.quit()
