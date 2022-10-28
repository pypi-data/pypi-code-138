#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2022/4/24 16:14
# @Author  : xgy
# @Site    : 
# @File    : check.py
# @Software: PyCharm
# @python version: 3.7.4
"""
import json
import os

from loguru import logger

from csp.datatool.utils import Entity


class EntityCheck(Entity):

    def __init__(self, folder, output=None):
        super(EntityCheck, self).__init__(folder, output)

    def check(self):
        """
        公共检查 text 字段值为空
        :return:
        """
        sources_error_l = []
        labelcategory_error_l = []
        # 检查字段全为空为空

        sources_flg = True
        labelcategorys_flg = True

        for index, item in enumerate(self.data):
            if item["id"]:
                if not item["text"]:
                    error_item = {"message": "the 'text' is empty", "data": {"id": item["id"]}}
                    sources_error_l.append(error_item)
            else:
                error_item = {"message": "the 'id' is empty", "data": item}
                sources_error_l.append(error_item)

            """
            公共检查 category 字段值为空
            """
            for tag in item["tags"]:
                if not item["category"] or not item["mention"]:
                    error_item = {"message": "the tag is empty", "data": {"id": item["id"], "tag": tag}}
                    labelcategory_error_l.append(error_item)

                if item["start"] < 0:
                    error_item = {"message": "the 'start' is error", "data": {"id": item["id"], "tag": tag}}
                    labelcategory_error_l.append(error_item)

        if labelcategory_error_l:
            save_path = os.path.join(self.output,
                                     "labelcategory_error.txt") if self.output else "labelcategory_error.txt"
            with open(save_path, "w", encoding="utf-8") as fw:
                for item in labelcategory_error_l:
                    fw.write(json.dumps(item, ensure_ascii=False))
                    fw.write("\n")
                logger.error("the category error information saved in  {}".format(save_path))
            labelcategorys_flg = False

        if sources_error_l:
            save_path = os.path.join(self.output, "text_error.txt") if self.output else "sources_error.txt"
            with open(save_path, "w", encoding="utf-8") as fw:
                for item in sources_error_l:
                    fw.write(json.dumps(item, ensure_ascii=False))
                    fw.write("\n")
                logger.error("the text error information saved in {}".format(save_path))
            sources_flg = False

        return sources_flg, labelcategorys_flg


def entity_check(folder, output=None):
    check_entity = EntityCheck(folder, output=output)
    check_entity.clean_output()
    check_entity.get_dataset()

    res = check_entity.check()


if __name__ == '__main__':
    print("start")
