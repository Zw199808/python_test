from selenium import webdriver
from selenium.webdriver.common.by import By

import time

# if __name__ == '__main__':
#      单个元素定位
#     driver = webdriver.Chrome()
#     driver.get("http://www.baidu.com")
#     # driver.find_element_by_id("kw").send_keys('大道至简')   #根据id定位元素
#     # driver.find_element_by_name("wd").send_keys('李中原')   #根据name定位元素
#     #driver.find_element_by_class_name('s_ipt').send_keys('hahaha')  #根据class_name定位元素，亲提示该class——name唯一
#     ##除此之外，还有xpath,cee_selector
#     # driver.find_element_by_xpath('//input[@id = "kw"]').send_keys('hahahah')  ## //表示相对路径，
#     # input是文本框的所在标签， @id=kw是文本框元素id的值，也可以将id换为其他的，name，class_name等
#     # driver.find_element_by_xpath('//form[@id="form"]/span/input').send_keys('hasdhjashd1')
#     # driver.find_element_by_xpath('//input[@id="kw" and @class="s_ipt"]').send_keys('hahahsh1')
#
#     # driver.find_element_by_css_selector('input#kw').send_keys('ashdhasd1') ##    #表示id,.表示class
#     driver.find_element_by_css_selector('form#form>span>input').send_keys('haks')
#
#     ###使用xpath时，用span/input来表示层级，使用css_selector时，用span>input,或者可不写：span input
#
#
#     time.sleep(5)
#     driver.quit()

# if __name__ == '__main__':
##多元素定位
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
# # li = driver.find_elements_by_css_selector('input[type = "hidden"]')[0].click()
# tag = driver.find_elements_by_tag_name('input')
# print(tag)
# for t in tag:
#     if t.get_attribute('autocomplete') == 'off':
#         t.send_keys('fighter007')
# driver.find_element_by_id("su").click()
# time.sleep(5)
# driver.quit()


# #使用By定位
# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.get("https://www.baidu.com")
#     driver.find_element(By.ID,"kw").send_keys("好大好大哈")
#     driver.find_element(By.ID,'kw').click()
#     time.sleep(5)
#     driver.quit()

# 使用 js 进行定位
# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.get("https://www.jianshu.com/sign_in")
#     time.sleep(2)
#     js_register = 'document.getElementById("js-sign-up-btn").click()'
#     driver.execute_script(js_register)
#     js_register_nickname = 'document.getElementByTagName("input")[3].name = "user[nickname]";'
#     time.sleep(2)
#     js_login = 'document.getElementsByTagName("a")[0].click()'
#     driver.execute_script(js_login)
#     time.sleep(2)
#     driver.quit()
#
# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.get('https://www.jianshu.com/sign_in')
#     time.sleep(1)
#     #定位登录页面
#     js_class = 'document.getElementsByClassName("active")[0].click();'
#     driver.execute_script(js_class)
#     time.sleep(1)
#     #定位账号输入框
#     js_account = 'document.getElementsByTagName("input")[2].vlaue = "username";'
#     driver.execute_script(js_account)
#     time.sleep(1)
#     #定位密码输入框
#     js_pwd = 'document.getElementsByTagName("input")[3].vlaue = "password";'
#     driver.execute_script(js_pwd)
#     time.sleep(1)
#     #定位登录按钮
#     js_login = 'document.querySelectorAll(".sign-in-button")[0].click;'
#     driver.execute_script(js_login)
#     time.sleep(2)
#     driver.quit()

