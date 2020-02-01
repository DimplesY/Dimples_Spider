'''
通过webdriver来操作百度进行查找
'''
from selenium import webdriver
import time


# 通过Keys模拟键盘
from selenium.webdriver.common.keys import Keys

# 操作哪个浏览器就建一个哪个浏览器的实例
# 自动通过环境变量来查找浏览器
driver = webdriver.PhantomJS()

# 如果浏览器没有配置相应的环境变量，则需要指定位置
driver.get("http://www.baidu.com")

print("Title:{}".format(driver.title))