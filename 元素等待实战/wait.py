# from selenium import webdriver
# import time
#
#
#
# #隐式定位
# if __name__ == '__main__':
#     #创建驱动
#     driver = webdriver.Chrome()
#     #驱动地址
#     driver.get("https://www.baidu.com")
#     #设置隐式等待5秒
#     driver.implicitly_wait(5)
#     driver.find_element_by_id('kw').send_keys('双击一下')
#     time.sleep(3)
#     driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By  #导入By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://mail.sina.com.cn/")
    element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID,"freename")))
    element.send_keys('hahahahah')
    time.sleep(5)

