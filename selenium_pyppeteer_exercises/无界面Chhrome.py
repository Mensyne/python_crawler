#-*- coding:utf-8 -*-
from selenium import webdriver
# 无界面的Chrome使用方法
options=webdriver.ChromeOptions()
options.set_headless()
# options.add_argument(‘--headless‘)
options.add_argument('--disable-gpu')
driver=webdriver.Chrome(options=options)
driver.get('http://httpbin.org/user-agent')
driver.get_screenshot_as_file('test.png')
driver.close()