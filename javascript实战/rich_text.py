from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time



#处理富文本
# if __name__ == '__main__':
#     dr = webdriver.Chrome()
#     url = 'https://nku.xiaokesi.com/system/newsAdd'
#     A = "hahah"
#     dr.get(url)
#     js = 'document.getElementsByClassName("public-DraftEditor-content")[0].contentWindow.document.' \
#          'body.innerHTML = "%s"'%(A)
#     dr.execute_script(js)
#     dr.quit()


# 处理隐藏元素
# if __name__ == '__main__':
#     dr = webdriver.Chrome()
#     url = "https://www.baidu.com"
#     dr.get(url)
#     time.sleep(2)
#     js = 'document.getElementById("s-user-setting-menu").style.display="block";' # 改变样式
#     dr.execute_script(js) # 执行js
#     print(1)
#     time.sleep(3)
#     dr.find_element_by_xpath('//*[@id="s-user-setting-menu"]/a[1]').click() # 点击隐藏的元素
#     time.sleep(3)
#     dr.quit()



#处理readonly属性
# if __name__ == '__main__':
#     dr = webdriver.Chrome()
#     url = "https://kyfw.12306.cn/otn/leftTicket/init"
#     dr.get(url)
#     time.sleep(2)
#     dr.find_element_by_id("qd_closeDefaultWarningWindowDialog_id").click()
#     # dr.switch_to.alert.accept() # 确认弹窗
#     js1 = 'document.getElementById("train_date").removeAttribute("readonly");' #获取控件，移除属性
#     dr.execute_script(js1)
#     print(1)
#     dr.find_element_by_id("train_date").clear() #清除数据
#     dr.find_element_by_id('train_date').send_keys('2021-06-09') # 设置最新数据
#     time.sleep(3)
#     dr.quit()



# execute_script()处理浏览器滚动条
# if __name__ == '__main__':
#     dr = webdriver.Chrome()
#     url = "https://baidu.com"
#     dr.get(url)
#     dr.find_element_by_id('kw').send_keys('selenium')
#     dr.find_element_by_id('su').click()
#     time.sleep(3)
#     dr.execute_script('window.scrollTo(0,10000);') # 执行第一次js代码
#     time.sleep(3)
#     dr.execute_script('window.scrollTo(10000,0)') # 执行第二次JS代码
#     time.sleep(3)
#     dr.quit()



# 使用Keys类中的DOWN，UP实现
if __name__ == '__main__':
    dr = webdriver.Chrome()
    dr.maximize_window()
    url = 'https://www.baidu.com'
    dr.get(url)
    dr.find_element_by_id('kw').send_keys('好奇')
    dr.find_element_by_id('su').click()
    time.sleep(4)
    dr.find_element_by_xpath('//*[@id="page"]/div/a[10]').send_keys(Keys.DOWN)    #设置向下滚动的元素的位置
    time.sleep(4)
    dr.find_element_by_xpath('//*[@id="s_tab"]/div/a[9]').send_keys(Keys.UP)    # 设置向上的元素的位置
    time.sleep(4)
    dr.quit()
















