
import requests
import pandas as pd
from pandas import ExcelWriter
from pyquery import PyQuery as pq

newstitle= []
newstime = []
newssite = []
newsshortcontent = []
newstages = []

def spider_crawler(url,headers):
    print("正在抓取网页中.......")
    response = requests.get(url,headers = headers)
    html = response.content
    doc = pq(html) ## 创建pyquery
    node_list = doc('div.newsitem__content').items()
    for node in node_list:
        title = node(".newsitem__title").text()
        site  = "https://fbs.com/" + node('.newsitem__content a').attr('href')
        time  = node('time').attr('datetime')
        smallcontent  = node('.newsitem__text p').text()
        tag = ','.join([i.text()  for i in node('.newsitem__tags a').items()])
        newstitle.append(title)
        newssite.append(site)
        newstime.append(time)
        newsshortcontent.append(smallcontent)
        newstages.append(tag)

def writer_excel():
    df = pd.DataFrame({'title':newstitle,
                       'site':newssite,
                       'time':newstime,
                       'content':newsshortcontent,
                       'tag':newstages})
    writer = ExcelWriter('result1.xlsx')
    df.to_excel(writer,'result',index =False)
    writer.save()

def run():
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
    try:
        print("开始....")
        for i in range(1,1000):
            url = f"https://fbs.com/analytics/news?page={i}&per-page=50"
            spider_crawler(url,headers)
        writer_excel()
        print("结束....")
    except Exception:
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    run()










