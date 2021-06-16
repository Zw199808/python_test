import unittest
from selenium import webdriver
import time


class TestWebUI(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_QQLogin(self):
        url = "https://mail.qq.com/cgi-bin/loginpage"
        self.driver.get(url)
        time.sleep(5)
        self.assertEqual(self.driver.title, '登录QQ邮箱', '页面跳转失败，请检查！')

    def test_MaoyanMovie(self):
        url = 'https://maoyan.com/'
        self.driver.get(url)
        time.sleep(5)
        self.assertEqual(self.driver.title, '猫眼电影 - 娱乐看猫眼', '页面跳转失败，请重新检查')


if __name__ == '__main__':
    unittest.main()