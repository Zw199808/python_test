from Myunit import *


class TestModel(TestWebUI):
    def test_QQLogin(self):
        url = "https://mail.qq.com/cgi-bin/loginpage"
        self.driver.get(url)
        self.assertEqual(self.driver.title, '登录QQ邮箱')

    def test_MaoYanMovie(self):
        url = "https://maoyan.com/"
        self.driver.get(url)
        self.assertEqual(self.driver.title, '猫眼电影 - 娱乐看猫眼')
