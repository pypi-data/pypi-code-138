#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2022/5/18 9:53
# @Author  : xgy
# @Site    : 
# @File    : dataset_server.py
# @Software: PyCharm
# @python version: 3.7.4
"""
import json
import os

# from csp.common.http_client import HttpClient
import sys

from csp.aip.common.http_client import HttpClient
from csp.common.config import Configure
from csp.common.utils import format


# from datetime import datetime


def data_list(name=None):
    interface_config = Configure().data
    http_client = HttpClient()

    url = interface_config["search"]["dataset"]
    params = {"name": name}
    res_dict = http_client.get(url, **params)

    # title_dict = {"名称": "name", "分类": "classify", "标注分类": "annotationType", "源数据": "rawDataNum", "训练数据": "trainDataNum", "验证数据": "evaDataNum",
    #               "创建时间": "createTime", "更新时间": "updateTime", "描述": "funDesc"}

    title_dict = {"名称": "name", "分类": "classify", "标注分类": "annotationType", "原始数据": "rawDataNum", "训练数据": "trainDataNum", "验证数据": "evaDataNum",
                  "功能描述": "funDesc"}

    format(res_dict, title_dict)


def data_get(name=None, infer_type: str = None, show=True):
    interface_config = Configure().data
    http_client = HttpClient()

    url = interface_config["search"]["dataset"]
    params = {"name": name}
    res_dict = http_client.get(url, **params)

    if infer_type == "list" or infer_type == "search":
        title_dict = {"名称": "name", "分类": "classify", "标注分类": "annotationType", "原始数据": "rawDataNum", "标注数据": "trainDataNum",
                      "验证数据": "evaDataNum", "功能描述": "funDesc"}

        string = format(res_dict, title_dict, show=show)

        if show:
            os.makedirs("/tmp", exist_ok=True)
            if sys.platform == "win32":
                code = "GBK"
            else:
                code = "utf-8"

            with open("/tmp/dataset_l.txt", "w", encoding=code) as fw:
                fw.write(repr(string))
            txt_abs = os.path.abspath("/tmp/dataset_l.txt")

            os.system("more " + txt_abs)

            return string

    if infer_type == "info":
        info_dict = {"名称": res_dict["data"][0]["name"],
                     "分类": res_dict["data"][0]["classify"],
                     "标注分类": res_dict["data"][0]["annotationType"],
                     "原始数据": res_dict["data"][0]["rawDataNum"],
                     "标注数据": res_dict["data"][0]["trainDataNum"],
                     "验证数据": res_dict["data"][0]["evaDataNum"],
                     "创建时间": res_dict["data"][0]["createTime"],
                     "更新时间": res_dict["data"][0]["updateTime"],
                     "描述": res_dict["data"][0]["funDesc"]}
        json_data = json.dumps(info_dict, ensure_ascii=False, indent=4)
        print(json_data)


def data_download(name, mode, size, output):
    interface_config = Configure().data
    http_client = HttpClient()

    # 按时间戳创建文件夹保存下载数据
    # create_time = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S%f")
    # output = os.path.join(output, create_time)
    # os.makedirs(output, exist_ok=True)

    # 停用，使用命令行时将不创建时间戳创建文件夹，便于后续代码集成
    # 按 mode 创建文件夹
    # 0923
    # 平台数据集名称命名修改，已不存在重名问题，删除按mode穿件文件夹功能
    # output = os.path.join(output, mode)
    os.makedirs(output, exist_ok=True)

    url = interface_config["download"]["dataset"]
    params = {"name": name, "mode": mode, "size": size}
    print("文件正在打包，请稍等。。。。。。")
    save_path = http_client.download(url, output, **params)

    return save_path


if __name__ == '__main__':
    print("start")
    # name = "中标通知书"
    # output = "C:/Users/xgy/Desktop/CSPTools/infetr_test/"

    data_list()
