import unittest
from selenium import webdriver


## 实例化浏览器和关闭浏览器
class TestWebUI(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()