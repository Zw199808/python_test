from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time



#根据switch_to.alert.text()获取弹窗信息
# if __name__ == '__main__':
#     dr = webdriver.Chrome()
#     url = "https://www.baidu.com"
#     dr.get(url)
#     action = ActionChains(dr) #模拟鼠标点击
#     setting = dr.find_element_by_id("s-usersetting-top") #获取设置控件
#     action.move_to_element(setting).perform() # 模拟指针悬停控件
#     time.sleep(3)
#     dr.find_element_by_link_text('搜索设置').click() # 获取搜索设置控件并点击
#     time.sleep(3)
#     dr.find_element_by_id('nr_3').click() # 获取选项并点击
#     time.sleep(3)
#     dr.find_element_by_class_name("prefpanelgo").click() #点击保存控件，触发弹窗
#     alert_text = dr.switch_to.alert.text # 保存弹窗内容
#     print(alert_text)# 输出
#     time.sleep(2)
#     dr.quit()


# #使用switch_to.alert.accept()接受警告框
# if __name__ == '__main__':
#     dr = webdriver.Chrome()
#     url = 'https://www.baidu.com'
#     action = ActionChains(dr)
#     dr.get(url)
#     setting = dr.find_element_by_id('s-usersetting-top') # 获取设置控件
#     action.move_to_element(setting).perform() # 模拟鼠标指针悬停
#     time.sleep(3)
#     dr.find_element_by_link_text('搜索设置').click() # 设置点击搜索设置
#     time.sleep(3)
#     dr.find_element_by_class_name('prefpanelgo').click() # 点击保存设置
#     time.sleep(5)
#     dr.switch_to.alert.accept()  # 确认弹窗按钮
#     time.sleep(2)
#     dr.quit()



# 使用switch_to.alert.dismiss()取消广告框
if __name__ == '__main__':
    dr = webdriver.Chrome()
    url = 'https://www.baidu.com'
    action = ActionChains(dr)
    dr.get(url)
    setting = dr.find_element_by_id('s-usersetting-top') #获取控件
    action.move_to_element(setting).perform() # 模拟鼠标指针悬停
    time.sleep(3)
    dr.find_element_by_link_text('搜索设置').click() # 点击搜索设置
    time.sleep(2)
    dr.find_element_by_class_name('prefpanelgo').click()# 点击保存设置
    time.sleep(3)
    dr.switch_to.alert.dismiss()  # 取消弹窗
    dr.quit()
