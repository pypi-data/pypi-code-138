#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2022/9/26 17:04
# @Author  : xgy
# @Site    : 
# @File    : eva.py
# @Software: PyCharm
# @python version: 3.7.4
"""
import os


def det_voc(submit_file, gold_folder, output):
    """
    目标检测任务评估（VOC格式数据）命令
    Parameters
    ----------
    submit_file : 预测结果json文件
    gold_folder : 答案文件夹(VOC)
    output : 评估结果保存目录

    Returns
    -------

    """
    os.makedirs(output, exist_ok=True)
    if not os.path.isfile(submit_file):
        raise FileNotFoundError("submit_file should be a file")
    if not os.path.isdir(gold_folder):
        raise FileNotFoundError("gold_folder should be a folder(voc)")

    from csp.datatool.image_detection.eva import det_eva
    try:
        det_eva(submit_file, gold_folder, form="voc", output=output)
    except Exception as ae:
        print(repr(ae))


def det_coco(submit_file, gold_folder, output):
    """
    目标检测任务评估（COCO格式数据）命令
    Parameters
    ----------
    submit_file : 预测结果json文件
    gold_folder : 答案文件夹(COCO)
    output : 评估结果保存目录

    Returns
    -------

    """
    os.makedirs(output, exist_ok=True)
    if not os.path.isfile(submit_file):
        raise FileNotFoundError("submit_file should be a file")
    if not os.path.isdir(gold_folder):
        raise FileNotFoundError("gold_folder should be a folder(coco)")

    from csp.datatool.image_detection.eva import det_eva
    try:
        det_eva(submit_file, gold_folder, form="coco", output=output)
    except Exception as ae:
        print(repr(ae))


def text_entity(submit_file, gold_file, output, long_text_categories: list = None):
    """
    文本实体抽取任务评估（平台格式数据）命令
    Parameters
    ----------
    submit_file : 预测结果json文件
    gold_file : 答案json文件
    long_text_categories : 长文本字段名称列表
    output : 评估结果保存目录

    Returns
    -------

    """
    if not os.path.isfile(gold_file):
        raise FileNotFoundError("gold_file should be a file")
    from csp.datatool.text_entity.eva import entity_eva
    try:
        entity_eva(submit_file, gold_file, output=output, long_text_categories=long_text_categories)
    except Exception as ae:
        print(repr(ae))


def text_entity_relation(submit_file, gold_file, output, long_text_categories: list = None):
    """
    本实体关系抽取任务评估（平台格式数据）命令
    Parameters
    ----------
    submit_file : 预测结果json文件
    gold_file : 答案json文件
    long_text_categories : 长文本字段名称列表
    output : 评估结果保存目录

    Returns
    -------

    """
    if not os.path.isfile(submit_file) or not os.path.isfile(gold_file):
        raise FileNotFoundError("submit_file and gold_file should be a file")
    from csp.datatool.text_entity_relation.spo_eva import spo_eva
    try:
        spo_eva(submit_file, gold_file, output=output, long_text_categories=long_text_categories)
    except Exception as ae:
        print(repr(ae))


def text_cls(submit_file, gold_folder, output):
    """
    文本分类任务评估（平台格式数据）命令
    Parameters
    ----------
    submit_file : 预测结果json文件
    gold_folder : 答案文件夹
    output : 评估结果保存目录

    Returns
    -------

    """
    from csp.datatool.text_classify.eva import text_classify_eva
    if not os.path.isdir(gold_folder):
        raise FileNotFoundError("gold_folder should be a folder")

    try:
        text_classify_eva(submit_file, gold_folder, output=output)
    except Exception as ae:
        print(repr(ae))


def img_cls(submit_file, gold_folder, output):
    """
    图像分类任务评估（平台格式数据）命令
    Parameters
    ----------
    submit_file : 预测结果txt文件
    gold_folder : 答案文件夹
    output : 评估结果保存目录

    Returns
    -------

    """
    from csp.datatool.image_classify.eva import img_classify_eva
    if not os.path.isdir(gold_folder):
        raise FileNotFoundError("gold_folder should be a folder")
    try:
        img_classify_eva(submit_file, gold_folder, output=output)
    except Exception as ae:
        print(repr(ae))


if __name__ == '__main__':
    print("start")
