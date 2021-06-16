from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

# #鼠标指针悬停
# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.get("https://www.baidu.com")
#     setting = driver.find_element_by_id("s-usersetting-top")
#     # 传入驱动进入ActionChains()方法，调用move_to_element(setting),最后使用perform()执行所有的动作。
#     ActionChains(driver).move_to_element(setting).perform()
#     time.sleep(3)
#     js_hot = "document.getElementsByClassName('setpref')[0].click()"
#     driver.execute_script(js_hot)
#     time.sleep(3)

# 鼠标右键实战
# if __name__ == '__main__':
#     #创建driver
#     driver = webdriver.Chrome()
#     #获取地址
#     driver.get("https://www.baidu.com")
#     time.sleep(2)
#     #定位百度一下控件
#     element = driver.find_element_by_id("su")
#     #模拟鼠标点击
#     ActionChains(driver).context_click(element).perform()
#     time.sleep(3)
#     driver.quit()

if __name__ == '__main__':
    #创建驱动
    driver = webdriver.Chrome()
    #驱动地址
    driver.get("https://www.baidu.com")
    time.sleep(2)
    #获取输入控件并输入高考
    driver.find_element_by_id("kw").send_keys('高考')
    #获取双击控件
    element = driver.find_element_by_id("su")
    #模拟鼠标双击
    ActionChains(driver).double_click(element).perform()
    time.sleep(5)
    driver.quit()

