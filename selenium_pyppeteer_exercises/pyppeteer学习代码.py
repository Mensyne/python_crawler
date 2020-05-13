#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:08:26 2020

@author: mensyne
"""

import asyncio
from pyppeteer import launch
from numpy import random

async def main():
    browser = await launch (
         executablePath = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
         headless = False,
         devtools = True,
         autoClose = False, ## js 渲染完后自动关闭浏览器
         args= ['--no-sandbox', ## 浏览器无限制
                '--disable-infobars', ## 隐藏正在受到自动软件的控制
                #'--proxy-server={}'.format(proxy) ## 可以放代理
                ],
        )
    page = await browser.newPage() ## 开启页面
    await page.setViewport({'width':1366,'height':800}) ## 设置页码大小
    await page.setJavaScriptEnabled(enabled = True) # 是否开启js
    await page.setUserAgent('Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36')
    
    res = await page.goto("https://www.baidu.com",options ={'timeout':10000}) ## 10超时
    await asyncio.sleep(2) ## 异步等待
    ## 在搜索框中输出python
    await page.type('input#kw.s_ipt','python 成功之路',{'delay':random.randint(100,151) -50}) ## 随机输入延迟
    ## 点击搜索按钮
    await page.clikc('input#su')
    await page.evaluate('window.scrollBy(0,window.innerHeight)') ## 滚动到页面底部
    ## Pypoeteer 三种解析方式
    """
    Page.querySelect() ## 选择器
    Page.querySelectAll() 
    Page.xpath() ## xpath 表达式
    简写成
    Page.J(),Page.JJ() and Page.Jx()
    """
    ## xpath 使用
    title_elements = await page.xpath('//h3[contains(@class,"t")]/a') ## 圈定元素
    for item in title_elements:
        title_str = await (await item.getProperty('textContent')).jsonValue()
        print(title_str)

    slider = await page.Jeval("#nocaptcha","node=>node.style") ## 判断是否有滑块
    print(res.status) ## 响应转态
    print(res.headers) ## 打印响应头
    print(await page.cookies()) ## 打印页面cookie
    print(await page.content()) ## 打印页面文本
    print(await page.title()) ## 打印当前页标题
    await page.screenshot({'path':'pic.png'}) ## 截屏幕保存
    await page.pdf(path="test_pdf.pdf") ##保存为pdf
    ## 在页面上执行js脚本
   #  dimensions = await page.evaluate('''() => {
   #  return{
   #      witdth:documentElement.clientWidth,
   #      height:document.documentElement.clientHeight,
   #      deviceScaleFactor:window.devicePixelRatio,
   #      }
   # }''',force_expr =True) ## force_expr =True 表示执行的是函数
   #
   #  print(dimensions)
   #  content = await page.evaluate(pageFunctions="document.body.textContent",force_expr = True) ## 只获取文本 执行js脚本

    ## iframe 时
    await asyncio.sleep(1)
    frame = page.frames
    print(frame) ## 需要找到是哪一个frame
    title = await frame[1].title()
    print(title)
    await asyncio.sleep(1)
    login = await frame[1].querySelector('#switcher_plogin')
    print(login)
    await login.click()
    await asyncio.sleep(2) #异步等待


    await  browser.close()

async def page_close(browser):
    for _page in await browser.pages():
        await _page.close()
    await browser.close


if __name__ == '__main__':
    ## 执行任务
    asyncio.get_event_loop().run_until_complete(main()) ## 启动单个任务
    ## 启动多个任务
    # url_list = url_list = [
    #     "http://www.baidu.com",
    #     "https://wap.huaqianapp.com/m/news/detail?id=17201398",
    #     "https://www.qq.com",
    # ]
    #
    #
    # taks = [main(url) for url in url_list]
    # loop = asyncio.get_event_loop()
    # results = loop.run_until_complete(asyncio.gather(*task))
    # for res in results:
    #     print(res)





















