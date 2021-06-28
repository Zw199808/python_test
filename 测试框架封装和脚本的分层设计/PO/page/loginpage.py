import sys
sys.path.append('../basePage')
from basePage.homeBase import HomePage
from selenium.webdriver.common.by import By
import time


# 定义页面类  继承HomePage
class LoginPage(HomePage):
    # 定义在登录中需要使用到的元素
    # 用户名
    username_loc = (By.NAME, 'account')

    # 密码
    password_loc = (By.NAME, 'pwd')

    # 登录按钮
    loginBtn_loc = (By.XPATH, '//*[@id="root"]/div/div/div/div/div/div/div/div[4]/button')

    # 用户名为空
    userNull_loc = (By.CSS_SELECTOR, ':after, :before')

    # 密码为空
    passwordNull_loc = (By.CSS_SELECTOR, ':after, :before')

    # 方法
    # 打开登录页面
    def openLoginPage(self):
        self.driver.get(self.url) # 打开地址
        self.driver.refresh() # 获取浏览器导航刷新按钮
        self.driver.maximize_window()
        time.sleep(2)

    # 输入用名
    def input_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)

    # 输入密码

    def input_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)

    # 点击登录

    def click_login_btn(self):
        self.find_element(*self.loginBtn_loc).click()

    # 用户名为空时候的提示
    def get_userNull(self):
        return self.find_element(*self.userNull_loc).text

    # 密码为空的提示
    def get_passwordNull(self):
        return self.find_element(*self.passwordNull_loc).text

    # 组装登录流程
    def login_gjs_pro(self,username,password):
        self.input_username(username)
        self.input_password(password)
        print(self.click_login_btn)
        self.click_login_btn()



