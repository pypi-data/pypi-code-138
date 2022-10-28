#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2022/9/26 15:49
# @Author  : xgy
# @Site    : 
# @File    : transform.py
# @Software: PyCharm
# @python version: 3.7.4
"""


def voc_coco(dataset, output):
    """
    目标检测任务VOC转COCO命令
    Parameters
    ----------
    dataset : 数据集目录
    output : 转换后数据保存目录

    Returns
    -------

    """
    from csp.datatool.image_detection.transform import det_transform
    try:
        det_transform(dataset, form="VOC", output=output)
        print("转换完成")
    except Exception as ae:
        print(repr(ae))


def coco_voc(dataset, output):
    """
    目标检测任务COCO转VOC命令
    Parameters
    ----------
    dataset : 数据集目录
    output : 转换后数据保存目录

    Returns
    -------

    """
    from csp.datatool.image_detection.transform import det_transform
    try:
        det_transform(dataset, form="COCO", output=output)
        print("转换完成")
    except Exception as ae:
        print(repr(ae))


# def std_doccano(dataset, output):
#     """
#     文本实体关系抽取任务平台数据格式转doccano格式命令
#     Parameters
#     ----------
#     dataset : 数据集目录
#     output : 转换后数据保存目录
#
#     Returns
#     -------
#
#     """
#     from csp.datatool.text_entity_relation.transform import spo_transform
#     try:
#         spo_transform(dataset, form="standard2doccano", output=output)
#         print("转换完成")
#     except Exception as ae:
#         print(repr(ae))


# def uie_std(dataset, uie_file, output):
#     """
#     文本实体关系抽取任务平台数据格式转doccano格式命令
#     Parameters
#     ----------
#     dataset : 数据集目录
#     uie_file : uie json 文件路径
#     output : 转换后数据保存目录
#
#     Returns
#     -------
#
#     """
#     from csp.datatool.text_entity_relation.transform import spo_transform
#     try:
#         spo_transform(dataset, form="uie2standard", output=output, uie_file=uie_file)
#         print("转换完成")
#     except Exception as ae:
#         print(repr(ae))


# def std_kg(dataset, output):
#     """
#     文本实体关系抽取任务平台标准数据集转知识图谱展示服务（csp kg）格式命令
#     Parameters
#     ----------
#     dataset : 数据集目录
#     output : 转换后数据保存目录
#
#     Returns
#     -------
#
#     """
#     from csp.datatool.text_entity_relation.transform import spo_transform
#     try:
#         spo_transform(dataset, form="standard2doccano", output=output)
#         print("转换完成")
#     except Exception as ae:
#         print(repr(ae))


def std_baiducls(dataset, output):
    """
    图像分类任务平台格式转百度格式数据命令
    Parameters
    ----------
    dataset : 数据集目录
    output : 转换后数据保存目录

    Returns
    -------

    """
    from csp.datatool.image_classify.transform import img_classify_transform
    try:
        img_classify_transform(dataset, output=output)
        print("转换完成")
    except Exception as ae:
        print(repr(ae))


def std_doccano_ner(dataset, output):
    """
    文本实体抽取任务平台数据格式转doccano格式命令
    Parameters
    ----------
    dataset : 数据集目录
    output : 转换后数据保存目录

    Returns
    -------

    """
    from csp.datatool.text_entity.transform import std_doccano
    try:
        std_doccano(dataset, output=output)
        print("转换完成")
    except Exception as ae:
        print(repr(ae))


if __name__ == '__main__':
    print("start")
