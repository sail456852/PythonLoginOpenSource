topic_url = 'https://www.douban.com/group/topic/208661235/'
# 失败了，不知道怎么切换到登录密码页面
import time
from selenium import webdriver

username = 'yourEmail'
password = 'yourPass'
# it works like smooth
driver = webdriver.Chrome('C:\\tools\\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.maximize_window()
driver.get('https://www.douban.com')

try:
    time.sleep(2)  # Let the user actually see something!
    # driver.find_element_by_class_name("account-tab-account").click()
    # driver.find_element_by_link_text("密码登录").click()
    # driver.find_element_by_id
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    time.sleep(5)
    driver.find_element_by_css_selector(".btn-active").click()
    time.sleep(5)  # Let the user actually see something!
except Exception:
    print('\nError exiting chrome')
    driver.quit()
