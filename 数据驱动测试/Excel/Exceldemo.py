import xlrd
import ddt,  unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 引入显示等待模块
from selenium.webdriver.support import expected_conditions as EC # 引入EC模块，expected_conditions

'''
WebDriverWait(driver,timeout,poll_frequency,ignored_exceptions),
driver：浏览器驱动
timeout：最长超时时间，默认以秒为单位
poll_frequency：检测的间隔步长，默认为0.5s
ignored_exceptions：超时后的抛出的异常信息，默认抛出NoSuchElementExeception异常。

与until()和until_not()结合使用：

WebDriverWait(driver,10).until(method，message="")
调用该方法提供的驱动程序作为参数，直到返回值为True
WebDriverWait(driver,10).until_not(method，message="")
调用该方法提供的驱动程序作为参数，直到返回值为False

与EC模块结合使用：
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

wait = WebDriverWait(driver,10,0.5)
element =wait.until(EC.presence_of_element_located((By.ID,"kw")),message="")
# 此处注意，如果省略message=“”，则By.ID外面是三层()

'''


# def readBook():
#     book = xlrd.open_workbook('datainfo.xlsx', 'r')
#     return book


def readUserName(row):
    book = xlrd.open_workbook('datainfo.xlsx', 'r')
    table = book.sheet_by_index(0)
    return table.row_values(row)[0]


def readUserPwd(row):
    book = xlrd.open_workbook('datainfo.xlsx', 'r')
    table = book.sheet_by_index(0)
    return table.row_values(row)[1]


def readAssertText(row):
    book = xlrd.open_workbook('datainfo.xlsx', 'r')
    table = book.sheet_by_index(0)
    return table.row_values(row)[2]


class TestSoHuLogin(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.testUrl = "https://mail.sohu.com/fe/#/login"

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def by_css(self, usernameloc): # 二次封装by_css
        return self.driver.find_element_by_css_selector(usernameloc)

    def getAassertText(self): #获取提示信息
        try:
            time.sleep(2)
            loctor = (By.CSS_SELECTOR,'.tipHolder.ng-binding')
            WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located((loctor)))
            return self.by_css('.tipHolder.ng-binding').text
        except Exception as message:
            print('元素定位出错！报错原因是：{}'.format(message))

    def sohuLogin(self,user,pwd): # 封装登录功能
        self.by_css('.addFocus.ipt-account.ng-pristine.ng-valid').send_keys(user)
        self.by_css('.addFocus.ng-pristine.ng-valid').send_keys(pwd)
        self.by_css('.btn-login.fontFamily').click()

    def test_sohuLogin_001(self):
        # 第一条测试用例,账号和密码为空，登录失败，
        self.driver.get(self.testUrl)
        time.sleep(3)
        self.sohuLogin(readUserName(1), readUserPwd(1))
        self.assertEqual(self.getAassertText(), readAssertText(1))

    def test_sohuLogin_002(self):
        # 第一条测试用例,账号正确和密码为空，登录失败，
        self.driver.get(self.testUrl)
        time.sleep(3)
        self.sohuLogin(readUserName(2), readUserPwd(2))
        self.assertEqual(self.getAassertText(), readAssertText(2))

    def test_sohuLogin_003(self):
        # 第一条测试用例,账号错误和密码为空，登录失败，
        self.driver.get(self.testUrl)
        time.sleep(3)
        self.sohuLogin(readUserName(3), readUserPwd(3))
        self.assertEqual(self.getAassertText(), readAssertText(3))

    def test_sohuLogin_004(self):
        # 第一条测试用例,账号为空和密码正确，登录失败，
        self.driver.get(self.testUrl)
        time.sleep(3)
        self.sohuLogin(readUserName(4), readUserPwd(4))
        self.assertEqual(self.getAassertText(), readAssertText(4))


if __name__ == '__main__':
    unittest.main()
