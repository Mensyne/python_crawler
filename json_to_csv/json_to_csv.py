#-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import json
import csv

def json_to_csv():
    json_file = open("tencent.json",'r')
    csv_file = open("tencent.csv",'w')
    # 读取json 文件的字符串，并返回python数据类型
    item_list = json.load(json_file)
    # 创建一个csv 文件
    csv_writer = csv.writer(csv_file)
    # 表头一层嵌套列表
    sheet_head = item_list[0].keys()
    # 表数据是两层嵌套的列表
    sheet_data = [item.values() for item in item_list]
    # 先写一行表头的部分
    csv_writer.writerow(sheet_head)
    # 再写多行表的数据部分
    csv_writer.writerows(sheet_data)
    # 关闭文件，保存数据
    csv_file.close()
    json_file.close()


if __name__ == '__main__':
    json_to_csv()







