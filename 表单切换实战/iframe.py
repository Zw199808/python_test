from selenium import webdriver
import time

# #单表单切换
# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.get("https://mail.qq.com/cgi-bin/loginpage")
#     time.sleep(3)
#     driver.switch_to.frame('login_frame') #切换进入iframe标签
#     driver.find_element_by_id("switcher_plogin").click()
#     time.sleep(3)
#     driver.find_element_by_name('u').send_keys('username')
#     driver.find_element_by_name('p').send_keys('password')
#     driver.find_element_by_id('login_button').click()
#     driver.switch_to.default_content() #退出iframe标签
#     time.sleep(5)

# 表单特殊情况处理
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://mail.qq.com/cgi-bin/loginpage')
    time.sleep(2)
    Xpath = driver.find_element_by_xpath("//*[@id='login_frame']")
    driver.switch_to.frame(Xpath)
    driver.find_element_by_id("switcher_plogin").click()
    driver.find_element_by_id('u').send_keys("username")
    driver.find_element_by_id('p').send_keys('password')
    driver.find_element_by_id('login_button').click()
    time.sleep(2)
    driver.quit()