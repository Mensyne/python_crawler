#-*- coding:utf-8 -*-
import requests
from lxml import etree
class TiebaSpider(object):
    def __init__(self):
        self.base_url  ="http://tieba.baidu.com"
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
        self.begin_page = int(raw_input("请输入起始页码"))
        self.end_page = int(raw_input("请输入结束页码"))
        self.tieba_name = raw_input("请输入要搜索的贴吧名")

    def send_request(self,url,data={}):
        response = requests.get(url,params=data,headers=self.headers)
        return response

    def parse_page(self,response):
        html = response.content
        html_obj = etree.HTML(html)
        link_list =html_obj.xpath('//a[@class="j_th_tit "]/@href')
        return link_list

    def parse_image(self,response):
        html = response.content
        html_obj = etree.HTML(html)
        image_link_list = html_obj.xpath('//img[@class="BDE_Image"]/@src')
        return image_link_list

    def write_image(self,resposne,filename):
        print '[INFO]:正在保存图片'+filename
        with open(filename,'wb') as f:
            f.write(resposne.content)

    def main(self):
        for page in range(self.begin_page,self.end_page+1):
            pn = (page-1)*50
            query_data ={'kw':self.tieba_name,'pn':pn}
            url = self.base_url+"/f?"
            try:
                response = self.send_request(url,query_data)
                page_link_list = self.parse_page(response)
                for link in page_link_list:
                    url =self.base_url+link
                    try:
                        response = self.send_request(url)
                        image_link_list = self.parse_image(response)
                        # 为每个图片做处理
                        for link in image_link_list:
                            response = self.send_request(link)
                            try:
                                self.write_image(response,link[-15:])
                            except:
                                print "[INFO]解析图片失败"+link
                    except:
                        print "[INFO]帖子解析失败"
            except Exception as e:
                print "[INFO]帖子列表解析失败"
        print "[INFO]图片下载成功，谢谢使用"


if __name__ == '__main__':
    Spider = TiebaSpider()
    Spider.main()


