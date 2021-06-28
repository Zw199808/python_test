import sys,unittest
sys.path.append('../page')
sys.path.append('../common')
from common.ownUnit import MyUnitTests
from page.loginpage import *


class TestLogin(MyUnitTests, LoginPage):
    '''
    TestLogin测试类继承MyUniTests类，通过它来对驱动的定义，浏览器的开启关闭，
    以及loginPage的实例化，由LoginPage类构造的loginPage对象来打开浏览器。完成登录操作业务

    '''

    def test_login(self):
        ''' 用户名和密码正确 '''

        self.loginPage.openLoginPage()
        self.loginPage.login_gjs_pro('admin', '123456')
        # self.assertEqual(self.loginPage.get_assert_login(),'登录成功')
        print('登录成功！')

    def test_user_null(self):
        ''' 用户名为空 '''
        self.loginPage.openLoginPage()
        self.loginPage.login_gjs_pro('', '123456')
        # self.assertEqual(self.loginPage.get_userNull(),'填写信息不全！')

    def test_password_nul(self):
        ''' 密码为空'''
        self.loginPage.openLoginPage()
        self.loginPage.login_gjs_pro('admin', '')
        # self.assertEqual(self.loginPage.get_passwordNull(),'用户名/密码错误')

    def test_user_password_null(self):
        '''用户名和密码均无'''
        self.loginPage.openLoginPage()
        self.loginPage.login_gjs_pro('', '')
        # self.assertEqual(self.loginPage.get_passwordNull(),' 信息填写不全！')


if __name__ == '__main__':
    unittest.main(verbosity=2)
    '''
    verbosity是一个选项,表示测试结果的信息复杂度，有0、1、2 三个值
0 (静默模式): 你只能获得总的测试用例数和总的结果 比如 总共10个 失败2成功8
1 (默认模式): 非常类似静默模式 只是在每个成功的用例前面有个“.” 每个失败的用例前面有个 “F”
2 (详细模式):测试结果会显示每个测试用例的所有相关的信息
并且 你在命令行里加入不同的参数可以起到一样的效果
加入 --quiet 参数 等效于 verbosity=0
加入--verbose参数等效于 verbosity=2
什么都不加就是 verbosity=1

    '''



