from selenium import webdriver
import time
from selenium.webdriver.common.by import By


# get方法切换
# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.get('https://baidu.com')
#     driver.find_element_by_id('kw').send_keys('滲透吧')
#     driver.find_element_by_id('su').click()
#     driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()
#     driver.get('https://tieba.baidu.com/f?kw=%C9%F8%CD%B8&fr=ala0&tpl=5')
#     time.sleep(5)
#     driver.find_element_by_link_text('进入贴吧').click()
#     time.sleep(5)
#     driver.quit()


# #switch方法
# if __name__ == '__main__':
#     dr = webdriver.Chrome()
#     url = 'https://www.so.com/'
#     dr.get(url)
#     time.sleep(2)
#     dr.find_element_by_link_text('360导航').click()
#     time.sleep(2)
#     #获取所有窗口
#     windows = dr.window_handles
#     print(windows)
#     #通过索引切换到第二个窗口
#     dr.switch_to.window(windows[1])
#     time.sleep(2)
#     dr.find_element_by_id("search-kw").send_keys('第二个')
#     time.sleep(1)
#     dr.switch_to.window(windows[0])
#     dr.find_element_by_id('input').send_keys('第一个')
#     time.sleep(4)
#     dr.quit()


