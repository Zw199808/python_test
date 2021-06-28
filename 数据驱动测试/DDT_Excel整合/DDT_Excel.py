import xlrd
import unittest,ddt
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def readData(): # 读取数据，处理数据
    book = xlrd.open_workbook('../Excel/datainfo.xlsx', 'r')
    table = book.sheet_by_index(0)
    newRows = []
    for rowValue in range(1,table.nrows):  # table.nrows 获取表格有效行
        print(rowValue)
        print(table.row_values(rowValue, 0, table.ncols)) # table.ncols 获取有效列，该方法返回该行中所有单元格的数据组成的列表
        newRows.append(table.row_values(rowValue, 0, table.ncols))
    return newRows

@ddt.ddt
class TestLogin(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.testUrl = 'https://mail.sohu.com/fe/#/login'

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def by_css(self,usernameloc):
        return self.driver.find_element_by_css_selector(usernameloc)

    def getassertText(self):

        try:
            time.sleep(2)
            loctor = (By.CSS_SELECTOR,'.tipHolder.ng-binding')
            WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located((loctor)))
            return self.by_css('.tipHolder.ng-binding').text
        except Exception as message:
            print('元素定位出错！报错原因是：{}'.format(message))

    @ddt.data(*readData())
    @ddt.unpack   #处理数据
    def test_sohuLogin(self,user,pwd,text):
        self.driver.get(self.testUrl)
        time.sleep(2)
        self.by_css('.addFocus.ipt-account.ng-pristine.ng-valid').send_keys(user)
        self.by_css('.addFocus.ng-pristine.ng-valid').send_keys(pwd)
        self.by_css('.btn-login.fontFamily').click()
        self.assertEqual(self.getassertText(), text)


if __name__ == '__main__':
    unittest.main()

























