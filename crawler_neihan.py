#-*- coding:utf-8 -*-
import requests
import re

class NeiHanSpider(object):

    def __init__(self):
        self.headers = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; by TSG)"}
        self.base_url = 'http://www.neihanpa.com/article/list_5_'
        self.page=1
        # 用来匹配网页的文本
        self.pattern_page= re.compile('<div class="f18 mb20">(.*?)</div>',re.S)
        # 处理无用的字符
        # u"\u3000".encode("utf-8") 表示匹配全角中文空格
        self.pattern_result = re.compile("<.*?>|&.*?;|\s|"+"\u3000".encode("utf-8"))

    def send_request(self,url):
        print(("[INFO]正在发送请求"+url))
        proxy = {"http":"http://maozhaojun:ntkn0npx@114.67.224.167:16819"}
        html = requests.get(url,headers = self.headers,proxies = proxy).content
        html  =html.decode("gbk").encode('utf-8')
        return html

    def parse_page(self,html):
        result_list = self.pattern_page.findall(html)
        return result_list

    def write_page(self,result_list):
        with open('dunzi.txt','a') as f:
            f.write("第"+str(self.page)+"页:\n")
            for result in result_list:
                content = self.pattern_result.sub("",result)
                print ("[INFO]正在保存文本.....")
                f.write(content+"\n")
            f.write("\n\n")

    def main(self):
        while True:
            full_url = self.base_url + str(self.page) + ".html"
            try:
                html = self.send_request(full_url)
                result_list = self.parse_page(html)
                self.write_page(result_list)
                self.page += 1
            except Exception as e:
                print(e)
                print("[ERROR]: 页面抓取失败" + full_url)

            command = input("按回车继续爬取（退出输入q）:")
            if command == 'q':
                print ("[INFO] 谢谢使用，再见!")
                break

if __name__ == '__main__':
    spider = NeiHanSpider()
    spider.main()








