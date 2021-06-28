import unittest,yaml
import time
from selenium import webdriver



def readYaml():
    f = open('data.yaml','r',encoding='utf-8')
    data = yaml.load(f)
    f.close()
    return data

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
            return self.by_css('.tipHolder.ng-binding').text
        except Exception as message:
            print('元素定位出错！报错原因是：{}'.format(message))


    def sohuLogin(self,user,password):
        self.by_css('.addFocus.ipt-account.ng-pristine.ng-valid').send_keys(user)
        self.by_css('.addFocus.ng-pristine.ng-valid').send_keys(password)
        self.by_css('.btn-login.fontFamily').click()

    def test_login_001(self):
        self.driver.get(self.testUrl)
        time.sleep(3)
        self.sohuLogin(readYaml()['userNull']['username'],readYaml()['userNull']['password'])
        self.assertEqual(self.getassertText(),readYaml()['userNull']['assertText'])

    def test_login_002(self):
        self.driver.get(self.testUrl)
        time.sleep(3)
        self.sohuLogin(readYaml()['passNull']['username1'],readYaml()['passNull']['password1'])
        self.assertEqual(self.getassertText(),readYaml()['passNull']['assertText1'])


if __name__ == '__main__':
    unittest.main()