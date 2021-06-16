from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

#使用Select中的value定位
# if __name__ == '__main__':
    # # 创建谷歌浏览器驱动
    # driver = webdriver.Chrome()
    # # 输入需要的地址
    # driver.get("file:///Users/zw/zw/python%20%20%E8%87%AA%E5%8A%A8%E5%8C%96%E6"
    #            "%B5%8B%E8%AF%95%E5%AD%A6%E4%B9%A0/%E5%89%8D%E7%AB%AF%E9%A1%B5%E9%9D%A2%E7"
    #            "%B4%A0%E6%9D%90/%E4%B8%8B%E6%8B%89%E6%A1%86%E5%AE%9E%E6%88%98/demo.html")
    # # 获取下拉框控件
    # element = driver.find_element(By.ID,"box")
    # # 根据value获取下拉框控件中的value = 01的选项。
    # Select(element).select_by_value('01')
    # # 利用睡眠来显示3秒
    # time.sleep(3)
    # # 关闭浏览器
    # driver.quit()


# # Select类index获取
# if __name__ == '__main__':
#     # 创建谷歌浏览器驱动
#     driver = webdriver.Chrome()
#     # 给驱动地址
#     driver.get("file:///Users/zw/zw/python%20%20%E8%87%AA%E5%8A%A8%E5%8C%96%E6"
#                "%B5%8B%E8%AF%95%E5%AD%A6%E4%B9%A0/%E5%89%8D%E7%AB%AF%E9%A1%B5%E9%9D%A2%E7"
#                "%B4%A0%E6%9D%90/%E4%B8%8B%E6%8B%89%E6%A1%86%E5%AE%9E%E6%88%98/demo.html")
#     # 获取下拉框控件element
#     element = driver.find_element(By.ID,"box")
#     # 将element放入Select类中，利用index方法定位
#     Select(element).select_by_index(1)
#     # # 利用睡眠来显示3秒
#     time.sleep(3)
#     # # 关闭浏览器
#     driver.quit()


# # visible_text属性定位
# if __name__ == '__main__':
#     # 创建谷歌浏览器驱动
#     driver = webdriver.Chrome()
#     # 输入地址
#     driver.get("file:///Users/zw/zw/python%20%20%E8%87%AA%E5%8A%A8%E5%8C%96%E6"
#                "%B5%8B%E8%AF%95%E5%AD%A6%E4%B9%A0/%E5%89%8D%E7%AB%AF%E9%A1%B5%E9%9D%A2%E7"
#                "%B4%A0%E6%9D%90/%E4%B8%8B%E6%8B%89%E6%A1%86%E5%AE%9E%E6%88%98/demo.html")
#     # 获取下载选择卡框控件
#     element = driver.find_element(By.ID,"box")
#     # 将element放入Select中，根据visible_text属性定位
#     Select(element).select_by_visible_text("005")
#     # 利用睡眠来显示3秒
#     time.sleep(3)
#     # 关闭浏览器
#     driver.quit()

# 二次获取定位
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("file:///Users/zw/zw/python%20%20%E8%87%AA%E5%8A%A8%E5%8C%96%E6"
               "%B5%8B%E8%AF%95%E5%AD%A6%E4%B9%A0/%E5%89%8D%E7%AB%AF%E9%A1%B5%E9%9D%A2%E7"
               "%B4%A0%E6%9D%90/%E4%B8%8B%E6%8B%89%E6%A1%86%E5%AE%9E%E6%88%98/demo.html")
    # 先获取控件，再次根据xpath获取元素
    driver.find_element_by_id("box").find_element_by_xpath("//*[@id='id3']").click()
    time.sleep(2)
    driver.quit()

