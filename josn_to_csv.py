# -*- coding:utf-8 -*-

# pip install csv
# Python的csv文件处理模块
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

import csv
import json


def json_to_csv():
    json_file = file("纸短情长.json", "r")
    item_list = json.load(json_file)

    csv_file = file("纸短情长.csv", "w")
    # 创建csv文件的读写对象
    csv_wirter = csv.writer(csv_file)

    # 包含所有表头数据的列表 []
    sheet_data = item_list[0].keys()
    # print sheet_data

    # data_list = []
    # for item in item_list:
    #    data_list.append(item.values())

    # 包含所有职位数据的大列表 [[], [], [], []] 里面每个小列表都是一条职位数据
    data_list = [item.values() for item in item_list]
    # print data_list


    # writerow 写入一行数据，参数是一个列表
    csv_wirter.writerow(sheet_data)
    # writerows 写入多行数据，参数是一个嵌套列表
    csv_wirter.writerows(data_list)

    csv_file.close()
    json_file.close()


    # data_dict = {num : num + 1 for num in range(0, 10)}

    # values()
    # items()


if __name__ == "__main__":
    json_to_csv()

