#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:48:05 2020

@author: mensyne
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time


def login_and_get_cookie(username,password,binary_location):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches',['enable-automation'])
    options.add_argument('--diable-gpu')
    ## 隐藏滚动条 应对一些特征页面
    options.add_argument('--hide-scrollbars')
    # 不加载图片
    options.add_argument("blink-settings=imagesEnabled=False")
     
    driver = webdriver.Chrome(binary_location,chorme_options = options)
    driver.maximize_window()
    driver.get("https://login.taobao.com")
    
    ## 设置显示等待
    wait = WebDriverWait(driver,10)
    wait.until(EC.presence_of_element_located((By.ID,'fm-login-id')))
    
    ## 进行填写
    user_input = driver.find_element_by_id("fm-login-id")
    user_input.send_keys(str(username))
    password_input = driver.find_element_by_id("fm-login-password")
    password_input.send_keys(str(password))
    time.sleep(1)
    
    ## 判断验证码 
    captcha = driver.find_element_by_id("nc_1_nlz")
    if captcha:
        button = driver.find_element_by_id('nc_1_n1z')
        ActionChains(driver).click_and_hold(button).perform()
        ActionChains(driver).move_by_offset(258,0)
        ActionChains(driver).release(button).perform()
        time.sleep(2)
    ## 点击登录按钮
    login_butt = driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button')
    login_butt.click()
    
    ## 进行判断是否登录成功
    user_name = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'site-nav-login-info-nick')))
    print(user_name.text)
    cookies = driver.get_cookies()
    
    return cookies

 
if __name__ == "__main__":
    cookies = login_and_get_cookie('xx', 'xx')
        
                                           
        
    
    


