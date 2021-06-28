from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time


class GJsProject():  # 测试类
    def __init__(self):
        self.driver = webdriver.Chrome()

    def openBrowser(self, url):  # 开启浏览器
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(2)

    def quitBrowser(self): # 关闭浏览器
        self.driver.quit()

    def by_link(self, locText): # 重写元素定位
        return self.driver.find_element(By.CLASS_NAME, locText)

    def by_css(self, loc): #  重写元素定位
        return self.driver.find_element(By.NAME, loc)

    def inputUser(self,loc,text): # 获取登录输入框
        self.by_css(loc).send_keys(text)

    def inputPwd(self,loc,text): # 获取密码输入框
        self.by_css(loc).send_keys(text)

    def loginBtn(self,locText): # 获取登录按钮
        self.by_link(locText).click()

    def assert_success_text(self,loc): # 断言
        return self.by_css(loc).text

    def login_gjs(self,url,loc1,loc2,locText,username,password): # 登录调用方法
        self.openBrowser(url)
        time.sleep(3)
        self.inputUser(loc1,username)
        time.sleep(2)
        self.inputPwd(loc2,password)
        time.sleep(2)
        self.loginBtn(locText)
        time.sleep(2)
        # if self.assert_success_text(loc4) == assertText:
        #     print('pass')
        # else:
        #     print('fail')


if __name__ == '__main__':

    t = GJsProject()
    url = 'http://rights.nkucxcy.com/systemTest/user/login'
    # loc1 = '.ant-input .login_input___SRkyH'
    loc1 = 'account'
    loc2 = 'pwd'
    locText = 'login_btn___c_WLu'
    username = 'admin'
    password = '123456'
    t.login_gjs(url,loc1,loc2,locText,username,password)


