import driver
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

headers = {
    "User-Agent": "123"
}
browser=webdriver.Firefox()
url = 'http://yy.jdyfy.com/login'
browser.get(url)
# 定位到账户的输入框
# browser.find_element_by_xpath('//input').send_keys('id')
# time.sleep(1)
# 向输入框中填入账户信息
username = browser.find_element(By.XPATH, '//nz-input-group[1]/input')
username.send_keys('18042207177')
# time.sleep(1)
password = browser.find_element(By.XPATH, '//nz-input-group[2]/input')
password.send_keys('Zinanc613613')
# 登录
sign_in = browser.find_element(By.XPATH, '//app-login/div/div/div[2]/div[2]/div[2]/button')
sign_in.click()
# 设置一个最大等待时间，等待页面加载完成，直到出现指定的元素
wait = WebDriverWait(driver, 10)  # 这里设置最大等待时间为10秒
element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[4]/div[5]/div/span[3]/a")))
element.click()

# time.sleep(1)
# # 跳转科室
# examination = browser.find_element(By.XPATH, '//app-new-home/div/div[2]/div[2]/div[2]/div[4]/div[5]/div/span[3]/a')
# examination.click()
# time.sleep(1)
# # 医生抢号
# doctor = browser.find_element(By.XPATH, '//app-new-home/div/div[2]/div[2]/div[2]/nz-tabset/div[2]/div[1]/div/div[9]')
# doctor.click()
# time.sleep(1)
# # 跳转日期
# day = browser.find_element(By.XPATH, '//app-new-home/div/div[2]/div[3]/div[2]/div/div[2]/div[2]/ul/li[5]')
# day.click()
# time.sleep(1)
# # 进行预约
# pre = browser.find_element(By.XPATH, '//app-new-home/div/div[2]/div[3]/div[2]/div[2]/div/div[1]/div[2]/ul/li[1]/button')
# pre.click()
#
# pre = browser.find_element(By.XPATH, '//div/div[2]/div[4]/div[1]/div[2]/button')
# pre.click()
# time.sleep(1)
# # 确认预约
# finish = browser.find_element(By.XPATH, '//app-confirm-appointment/div[3]/div[2]/div/div[3]/button')
# finish.click()
# time.sleep(1)
