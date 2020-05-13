#-*- coding:utf-8 -*-
import random
import time
from bs4 import BeautifulSoup
import requests
import json


class TencentSpider(object):
    def __init__(self):
        self.base_url = "https://hr.tencent.com/position.php?&start=0"
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.item_list =[]
        self.page=1


    def send_request(self,url):
        response = requests.get(self.base_url,headers = self.headers)
        return response

    def parser_page(self,response):
        html = response.content
        soup = BeautifulSoup(html, "lxml")
        # 获取十位职位的每个节点
        node_list = soup.select('.even,.odd')
        # 迭代找打每个节点，然后取出每条职位的数据
        for node in node_list:
            item = {}
            item['position_name'] = node.select('td a')[0].get_text()
            item["position_linke"] = 'https://hr.tencent.com/'+node.select('td a')[0].get('href')
            item['position_type'] = node.select('td')[1].get_text()
            item['position_number'] = node.select('td')[2].get_text()
            item['work_location'] = node.select('td')[3].get_text()
            item['publish_time'] = node.select('td')[4].get_text()
            self.item_list.append(item)
        # 如果找到，则返回数据，如果没有找到则返回None
        if soup.find('a',{"class":"noactive","id":"next"}):
            return None
        else:
            # 获取下一页链接
            next_link = "https://hr.tencent.com/" + soup.find("a", {"id": "next"}).get("href")
            return next_link

    def write_page(self):
        json.dump(self.item_list,open('tencent.json','w'))

    def main(self):
        # 发送第一页的请求
        response = self.send_request(self.base_url)
        #发送下一页的请求
        while self.page <5:
            next_link = self.parser_page(response)
            if next_link is None:
                print("到了最后一页了")
                break
            else:
                try:
                    response = self.send_request(next_link)
                except:
                    print('[Error]解析下一页失败'+next_link)
                time.sleep(random.randint(1,3))
        self.write_page()

if __name__ == '__main__':
    Spider=TencentSpider()
    Spider.main()




