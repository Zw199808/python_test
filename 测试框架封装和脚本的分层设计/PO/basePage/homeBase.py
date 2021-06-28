from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 基础类
class HomePage(object):
    # 构造方法
    def __init__(self, url, driver):
        self.url = url
        self.driver = driver

    # 封装元素定位

    def find_element(self,  *loc):

        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc)) # 判断元素是否存在
            return self.driver.find_element(*loc)
        except Exception as message:
            print('元素无法在页面中找到:{}'.format(message))

