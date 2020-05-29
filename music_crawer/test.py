
import sys
import requests
import pandas as pd
from pyquery import PyQuery as pq
from pandas import ExcelWriter
import re
import os
os.chdir('/Users/mensyne/Desktop/python_crawler/music_crawer')


downlinks = []
singers =[]
musics = []
baidulinks = []
baidupasswds =[]

def spider_crawler(url,headers):
    print('正在抓取.......')
    response  = requests.get(url,headers = headers)
    html = response.content
    doc = pq(html)
    node_list = doc('table.songlist').items()
    for node in node_list:
        for i in  node('.st').items():
            musics.append(i.text())
        for j in node('tr>td:nth-child(2)>a').items():
            singers.append(j.text())
        for k in node('.dw').items():
            downlink = "https://www.sq688.com"+k.attr('href')
            response_url2 = requests.get(downlink,headers = headers)
            html2  =response_url2.content
            doc2 = pq(html2)
            baidudownlink = doc2('p.downurl').text()
            bdlink = re.sub('链接:|密码.*|提取码.*','',baidudownlink).strip()
            bdpasswd = re.search(r'(密码: (\w{4,}))|(密码:(\w{4,}))|(提取码: (\w{4,}))|(提取码:(\w{4,}))',baidudownlink).group().strip()
            bdpasswd = re.sub('密码:|提取码:','',bdpasswd).strip()
            baidulinks.append(bdlink)
            baidupasswds.append(bdpasswd)
            downlinks.append(downlink)




def wirter_excel():
    df = pd.DataFrame({'musicname':musics,
            'singer':singers,
            'downlinks':downlinks,
            'baidulink':baidulinks,
            'baidupasswd':baidupasswds})
    writer = ExcelWriter('result.xlsx')
    df.to_excel(writer,'result',index=False)
    writer.save()

def run():
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
    try:
        print('开始....')
        for i in range(1,11):
            for j in ['周杰伦','汪苏泷']:
                url = f"https://www.sq688.com/search.php?key={j}&page={i}"
                spider_crawler(url,headers)
        wirter_excel()
        print('结束....')
    except Exception:
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    run()








