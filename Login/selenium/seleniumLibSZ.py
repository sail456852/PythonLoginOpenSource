import time
from selenium import webdriver

username = 'yourUsername'
password = 'yourPass'
# it works like smooth
driver = webdriver.Chrome('C:\\tools\\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://libyy.utsz.edu.cn/login.html');
time.sleep(5)  # Let the user actually see something!
driver.find_element_by_id("inputUsername").send_keys(username)
driver.find_element_by_id("inputPwd").send_keys(password)
driver.find_element_by_id("inputVerifycode").send_keys("AAAA")
time.sleep(5)
driver.find_element_by_css_selector(".login_btn").click()
time.sleep(5)  # Let the user actually see something!
# driver.quit()
