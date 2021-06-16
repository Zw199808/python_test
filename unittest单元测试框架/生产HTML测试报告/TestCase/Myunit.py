from selenium import webdriver
import unittest


class TestWebUI(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls) -> None:  # 开启浏览器
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls) -> None:  # 关闭浏览器
        cls.driver.quit()
