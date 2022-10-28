#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2022/4/24 10:17
# @Author  : xgy
# @Site    : 
# @File    : datatool_cli.py
# @Software: PyCharm
# @python version: 3.7.4
"""

import os
import click
from csp.command.cli import csptools


# 一级命令 csp datatool
@csptools.group("datatool")
def datatool():
    """
    数据集处理命令，包括数据集转换、切分等子命令

    \b
    csp datatool 'commands' -h 获取子命令使用帮助
    """


##  二级命令
## 数据集切分 csp datatool split
@datatool.group("split")
def split():
    """
    数据集切分命令

    \b
    csp datatool split 'commands' -h 获取子命令使用帮助
    """


### 三级命令
### csp datatool split det-voc
@split.command()
@click.option("-d", "--dataset", prompt="数据集目录", help="数据集目录", required=True)
@click.option("-r", "--ratio", type=float, prompt="切分后训练数据比例", help="切分后训练数据比例", required=True)
@click.option("-m", "--mode", type=click.Choice(['train', 'trainval']), help="切分依据，当同时存在train.txt、trainval.txt文件时，指定其一", default=None, show_default=True)
def det_voc(dataset, ratio, mode):
    """
    目标检测任务VOC数据集切分命令

    \b
    使用示例：csp datatool split det-voc -d '数据集目录' -r '切分后训练数据比例' -m '切分依据'
    """
    from csp.datatool.image_detection.split import det_split
    try:
        det_split(folder=dataset, form="voc", ratio=ratio, mode=mode)
    except Exception as ae:
        print(repr(ae))


### 三级命令
### csp datatool split det-coco
@split.command()
@click.option("-d", "--dataset", prompt="数据集目录", help="数据集目录", required=True)
@click.option("-r", "--ratio", type=float, prompt="切分后训练数据比例", help="切分后训练数据比例", required=True)
@click.option("-m", "--mode", type=click.Choice(['train', 'trainval']), help="切分依据，当同时存在train.json、trainval.json文件时，指定其一", default=None, show_default=True)
def det_coco(dataset, ratio, mode):
    """
    目标检测任务COCO数据集切分命令

    \b
    使用示例：csp datatool split det-coco -d '数据集目录' -r '切分后训练数据比例' -m '切分依据'
    """
    from csp.datatool.image_detection.split import det_split
    try:
        det_split(folder=dataset, form="coco", ratio=ratio, mode=mode)
    except Exception as ae:
        print(repr(ae))


### 三级命令
### csp datatool split text-entity
@split.command()
@click.option("-d", "--dataset", prompt="数据集目录", help="数据集目录", required=True)
@click.option("-r", "--ratio", type=float, prompt="切分后训练数据比例", help="切分后训练数据比例", required=True)
@click.option("-o", "--output", prompt="切分后数据保存目录", help="切分后数据保存目录", required=True)
def text_entity(dataset, ratio, output):
    """
    文本实体抽取任务平台格式数据集切分命令

    \b
    使用示例：csp datatool split text-entity -d '数据集目录' -r '切分后训练数据比例'
    """
    from csp.datatool.text_entity.split import entity_split
    try:
        entity_split(folder=dataset, ratio=ratio, output=output)
    except Exception as ae:
        print(repr(ae))


### 三级命令
### csp datatool split text-entity-relation
@split.command()
@click.option("-d", "--dataset", prompt="数据集目录", help="数据集目录", required=True)
@click.option("-r", "--ratio", type=float, prompt="切分后训练数据比例", help="切分后训练数据比例", required=True)
@click.option("-o", "--output", prompt="切分后数据保存目录", help="切分后数据保存目录", required=True)
def text_entity_relation(dataset, ratio, output):
    """
    文本实体关系抽取任务平台格式数据集切分命令

    \b
    使用示例：csp datatool split text-entity-relation -d '数据集目录' -r '切分后训练数据比例'
    """
    from csp.datatool.text_entity_relation.split import spo_split
    try:
        spo_split(folder=dataset, ratio=ratio, output=output)
    except Exception as ae:
        print(repr(ae))


### 三级命令
### csp datatool split text-cls
@split.command()
@click.option("-d", "--dataset", prompt="数据集目录", help="数据集目录", required=True)
@click.option("-r", "--ratio", type=float, prompt="切分后训练数据比例", help="切分后训练数据比例", required=True)
def text_cls(dataset, ratio):
    """
    文本分类任务平台格式数据集切分命令

    \b
    使用示例：csp datatool split text-cls -d '数据集目录' -r '切分后训练数据比例'
    """
    from csp.datatool.text_classify.split import text_classify_split
    try:
        text_classify_split(folder=dataset, ratio=ratio)
    except Exception as ae:
        print(repr(ae))


### 三级命令
### csp datatool split img-cls
@split.command()
@click.option("-d", "--dataset", prompt="数据集目录", help="数据集目录", required=True)
@click.option("-r", "--ratio", type=float, prompt="切分后训练数据比例", help="切分后训练数据比例", required=True)
def img_cls(dataset, ratio):
    """
    图像分类任务平台格式数据集切分命令

    \b
    使用示例：csp datatool split img-cls -d '数据集目录' -r '切分后训练数据比例'
    """
    from csp.datatool.image_classify.split import img_classify_split
    try:
        img_classify_split(folder=dataset, ratio=ratio)
    except Exception as ae:
        print(repr(ae))


## 二级命令
## 数据集转换 csp datatool transform
@datatool.group("transform")
def transform():
    """
    数据集转换命令

    \b
    csp datatool transform 'commands' -h 获取子命令使用帮助
    """


## 三级命令
## 数据集转换 csp datatool transform voc-coco
@transform.command()
@click.option("-d", "--dataset", prompt="数据集目录", help="数据集目录", required=True)
@click.option("-o", "--output", prompt="转换后数据保存目录", help="转换后数据保存目录", required=True)
def voc_coco(dataset, output):
    """
    目标检测任务VOC转COCO命令

    \b
    使用示例：csp datatool transform voc-coco -d '数据集目录' -o '保存目录'
    """
    from csp.datatool.image_detection.transform import det_transform
    try:
        det_transform(dataset, form="VOC", output=output)
        print("转换完成")
    except Exception as ae:
        print(repr(ae))


## 三级命令
## 数据集转换 csp datatool transform coco-voc
@transform.command()
@click.option("-d", "--dataset", prompt="数据集目录", help="数据集目录", required=True)
@click.option("-o", "--output", prompt="转换后数据保存目录", help="转换后数据保存目录", required=True)
def coco_voc(dataset, output):
    """
    目标检测任务COCO转VOC命令

    \b
    使用示例：csp datatool transform coco-voc -d '数据集目录' -o '保存目录'
    """
    from csp.datatool.image_detection.transform import det_transform
    try:
        det_transform(dataset, form="COCO", output=output)
        print("转换完成")
    except Exception as ae:
        print(repr(ae))


## 三级命令
## 数据集转换 csp datatool transform std-doccano
# @transform.command()
# @click.option("-d", "--dataset", prompt="数据集目录", help="数据集目录", required=True)
# @click.option("-o", "--output", prompt="转换后数据保存目录", help="转换后数据保存目录", required=True)
# def std_doccano(dataset, output):
#     """
#     文本实体关系抽取任务平台数据格式转doccano格式命令
#
#     \b
#     使用示例：csp datatool transform std-doccano -d '数据集目录' -o '保存目录'
#     """
#     from csp.datatool.text_entity_relation.transform import spo_transform
#     try:
#         spo_transform(dataset, form="standard2doccano", output=output)
#         print("转换完成")
#     except Exception as ae:
#         print(repr(ae))


## 三级命令
## 数据集转换 csp datatool transform uie-std
# @transform.command()
# @click.option("-d", "--dataset", prompt="数据集目录", help="数据集目录", required=True)
# @click.option("-i", "--uie_file", help="uie json 文件路径", required=True)
# @click.option("-o", "--output", prompt="转换后数据保存目录", help="转换后数据保存目录", required=True)
# def uie_std(dataset, uie_file, output):
#     """
#     文本实体关系抽取任务UIE格式转平台标准数据集格式命令
#
#     \b
#     使用示例：csp datatool transform uie-std -d '数据集目录' -i 'uie json 文件' -o '保存目录'
#     """
#     from csp.datatool.text_entity_relation.transform import spo_transform
#     try:
#         spo_transform(dataset, form="uie2standard", output=output, uie_file=uie_file)
#         print("转换完成")
#     except Exception as ae:
#         print(repr(ae))


## 三级命令
## 数据集转换 csp datatool transform std-kg
# @transform.command()
# @click.option("-d", "--dataset", prompt="数据集目录", help="数据集目录", required=True)
# @click.option("-o", "--output", prompt="转换后数据保存目录", help="转换后数据保存目录", required=True)
# def std_kg(dataset, output):
#     """
#     文本实体关系抽取任务平台标准数据集转知识图谱展示服务（csp kg）格式命令
#
#     \b
#     使用示例：csp datatool transform std-kg -d '数据集目录' -o '保存目录'
#     """
#     from csp.datatool.text_entity_relation.transform import spo_transform
#     try:
#         spo_transform(dataset, form="standard2kg", output=output)
#         print("转换完成")
#     except Exception as ae:
#         print(repr(ae))


## 三级命令
## 数据集转换 csp datatool transform std-baiducls
@transform.command()
@click.option("-d", "--dataset", prompt="数据集目录", help="数据集目录", required=True)
@click.option("-o", "--output", prompt="转换后数据保存目录", help="转换后数据保存目录", required=True)
def std_baiducls(dataset, output):
    """
    图像分类任务平台标准数据集转百度数据格式命令

    \b
    使用示例：csp datatool transform std-baiducls -d '数据集目录' -o '保存目录'
    """
    from csp.datatool.image_classify.transform import img_classify_transform
    try:
        img_classify_transform(dataset, output=output)
        print("转换完成")
    except Exception as ae:
        print(repr(ae))


## 三级命令
## 数据集转换 csp datatool transform std-doccano-ner
@transform.command()
@click.option("-d", "--dataset", prompt="数据集目录", help="数据集目录", required=True)
@click.option("-o", "--output", prompt="转换后数据保存目录", help="转换后数据保存目录", required=True)
def std_doccano_ner(dataset, output):
    """
    文本实体抽取任务平台数据格式转doccano格式命令

    \b
    使用示例：csp datatool transform std-doccano-ner -d '数据集目录' -o '保存目录'
    """
    from csp.datatool.text_entity.transform import std_doccano
    try:
        std_doccano(dataset, output=output)
        print("转换完成")
    except Exception as ae:
        print(repr(ae))


## 二级命令
## 数据集检查 csp datatool check
@datatool.group("check")
def check():
    """
    数据集检查命令

    \b
    csp datatool check 'commands' -h 获取子命令使用帮助
    """


## 三级命令
## 数据集检查 csp datatool check det-voc
@check.command()
@click.option("-d", "--dataset", prompt="数据集目录", help="数据集目录", required=True)
@click.option("-o", "--output", prompt="检查结果保存目录", help="检查结果保存目录", required=True)
def det_voc(dataset, output):
    """
    目标检测任务VOC数据集检查命令

    \b
    使用示例：csp datatool check det-voc -d '数据集目录' -o '保存目录'
    """
    from csp.datatool.image_detection.check import det_check
    try:
        det_check(dataset, form="voc", output=output)
    except Exception as ae:
        print(repr(ae))


## 三级命令
## 数据集检查 csp datatool check det-coco
@check.command()
@click.option("-d", "--dataset", prompt="数据集目录", help="数据集目录", required=True)
@click.option("-o", "--output", prompt="检查结果保存目录", help="检查结果保存目录", required=True)
def det_coco(dataset, output):
    """
    目标检测任务COCO数据集检查命令

    \b
    使用示例：csp datatool check det-coco -d '数据集目录' -o '保存目录'
    """
    from csp.datatool.image_detection.check import det_check
    try:
        det_check(dataset, form="coco", output=output)
    except Exception as ae:
        print(repr(ae))


## 三级命令
## 数据集检查 csp datatool check text-entity
@check.command()
@click.option("-d", "--dataset", prompt="数据集目录", help="数据集目录", required=True)
@click.option("-o", "--output", prompt="检查结果保存目录", help="检查结果保存目录", required=True)
def text_entity(dataset, output):
    """
    文本实体抽取任务平台数据集检查命令

    \b
    使用示例：csp datatool check text-entity -d '数据集目录' -o '保存目录'
    """
    from csp.datatool.text_entity.check import entity_check
    try:
        entity_check(dataset, output=output)
    except Exception as ae:
        print(repr(ae))


## 三级命令
## 数据集检查 csp datatool check text-entity-relation
@check.command()
@click.option("-d", "--dataset", prompt="数据集目录", help="数据集目录", required=True)
@click.option("-o", "--output", prompt="检查结果保存目录", help="检查结果保存目录", required=True)
def text_entity_relation(dataset, output):
    """
    文本实体关系抽取任务平台数据集检查命令

    \b
    使用示例：csp datatool check text-entity-relation -d '数据集目录' -o '保存目录'
    """
    from csp.datatool.text_entity_relation.check import spo_check
    try:
        spo_check(dataset, output=output)
    except Exception as ae:
        print(repr(ae))


## 三级命令
## 数据集检查 csp datatool check text-cls
@check.command()
@click.option("-d", "--dataset", prompt="数据集目录", help="数据集目录", required=True)
@click.option("-o", "--output", prompt="检查结果保存目录", help="检查结果保存目录", required=True)
def text_cls(dataset, output):
    """
    文本分类任务平台数据集检查命令

    \b
    使用示例：csp datatool check text-cls -d '数据集目录' -o '保存目录'
    """
    from csp.datatool.text_classify.check import text_classify_check
    try:
        text_classify_check(dataset, output=output)
    except Exception as ae:
        print(repr(ae))


## 三级命令
## 数据集检查 csp datatool check img-cls
@check.command()
@click.option("-d", "--dataset", prompt="数据集目录", help="数据集目录", required=True)
@click.option("-o", "--output", prompt="检查结果保存目录", help="检查结果保存目录", required=True)
def img_cls(dataset, output):
    """
    图像分类任务平台数据集检查命令

    \b
    使用示例：csp datatool check img-cls -d '数据集目录' -o '保存目录'
    """
    from csp.datatool.image_classify.check import img_classify_check
    try:
        img_classify_check(dataset, output=output)
    except Exception as ae:
        print(repr(ae))


## 二级命令
## 预测结果评估 eva
@datatool.group("eva")
def eva():
    """
    数据评估命令

    \b
    csp datatool eva 'commands' -h 获取子命令使用帮助
    """


## 三级命令
## 预测结果评估 csp datatool eva det-voc
@eva.command()
@click.option("-i", "--submit_file", prompt="预测结果json文件", help="预测结果json文件", required=True)
@click.option("-g", "--gold_folder", prompt="答案文件夹(VOC)", help="答案文件夹(VOC)", required=True)
@click.option("-o", "--output", prompt="评估结果保存目录", help="评估结果保存目录", required=True)
def det_voc(submit_file, gold_folder, output):
    """
    目标检测任务评估（VOC格式数据）命令

    \b
    使用示例：csp datatool eva det-voc -i '预测结果' -g '答案文件夹' -o '保存目录'
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


## 三级命令
## 预测结果评估 csp datatool eva det-coco
@eva.command()
@click.option("-i", "--submit_file", prompt="预测结果json文件", help="预测结果json文件", required=True)
@click.option("-g", "--gold_folder", prompt="答案文件夹(coco)", help="答案文件夹(coco)", required=True)
@click.option("-o", "--output", prompt="评估结果保存目录", help="评估结果保存目录", required=True)
def det_coco(submit_file, gold_folder, output):
    """
    目标检测任务评估（COCO格式数据）命令

    \b
    使用示例：csp datatool eva det-coco -i '预测结果' -g '答案文件夹' -o '保存目录'
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


## 三级命令
## 预测结果评估 csp datatool eva text-entity
@eva.command()
@click.option("-i", "--submit_file", prompt="预测结果json文件", help="预测结果json文件", required=True)
@click.option("-g", "--gold_file", prompt="答案json文件", help="答案json文件", required=True)
@click.option("-o", "--output", prompt="评估结果保存目录", help="评估结果保存目录", required=True)
@click.argument('long_text_categories', nargs=-1)
def text_entity(submit_file, gold_file, long_text_categories, output):
    """
    文本实体抽取任务评估（平台格式数据）命令

    \b
    使用示例：csp datatool eva text-entity -i '预测结果json文件' -g '答案json文件' -o '保存目录' '长文本字段名称' '长文本字段名称'
    """
    if not os.path.isfile(gold_file):
        raise FileNotFoundError("gold_file should be a file")
    from csp.datatool.text_entity.eva import entity_eva
    try:
        entity_eva(submit_file, gold_file, output=output, long_text_categories=long_text_categories)
    except Exception as ae:
        print(repr(ae))


## 三级命令
## 预测结果评估 csp datatool eva text-entity-relation
@eva.command()
@click.option("-i", "--submit_file", prompt="预测结果json文件", help="预测结果json文件", required=True)
@click.option("-g", "--gold_file", prompt="答案json文件", help="答案json文件", required=True)
@click.option("-o", "--output", prompt="评估结果保存目录", help="评估结果保存目录", required=True)
@click.argument('long_text_categories', nargs=-1)
def text_entity_relation(submit_file, gold_file, long_text_categories, output):
    """
    文本实体关系抽取任务评估（平台格式数据）命令

    \b
    使用示例：csp datatool eva text-entity-relation -i '预测结果json文件' -g '答案json文件' -o '保存目录' '长文本字段名称' '长文本字段名称'
    """
    if not os.path.isdir(submit_file) or not os.path.isfile(gold_file):
        raise FileNotFoundError("submit_file and gold_file should be a file")
    from csp.datatool.text_entity_relation.spo_eva import spo_eva
    try:
        spo_eva(submit_file, gold_file, output=output, long_text_categories=long_text_categories)
    except Exception as ae:
        print(repr(ae))


## 三级命令
## 预测结果评估 csp datatool eva text-cls
@eva.command()
@click.option("-i", "--submit_file", prompt="预测结果json文件", help="预测结果json文件", required=True)
@click.option("-g", "--gold_folder", prompt="答案文件夹", help="答案文件夹", required=True)
@click.option("-o", "--output", prompt="评估结果保存目录", help="评估结果保存目录", required=True)
def text_cls(submit_file, gold_folder, output):
    """
    文本分类任务评估（平台格式数据）命令

    \b
    使用示例：csp datatool eva text-cls -i '预测结果' -g '答案文件夹' -o '保存目录'
    """
    from csp.datatool.text_classify.eva import text_classify_eva
    if not os.path.isdir(gold_folder):
        raise FileNotFoundError("gold_folder should be a folder")

    try:
        text_classify_eva(submit_file, gold_folder, output=output)
    except Exception as ae:
        print(repr(ae))


## 三级命令
## 预测结果评估 csp datatool eva img-cls
@eva.command()
@click.option("-i", "--submit_file", prompt="预测结果txt文件", help="预测结果txt文件", required=True)
@click.option("-g", "--gold_folder", prompt="答案文件夹", help="答案文件夹", required=True)
@click.option("-o", "--output", prompt="评估结果保存目录", help="评估结果保存目录", required=True)
def img_cls(submit_file, gold_folder, output):
    """
    图像分类任务评估（平台格式数据）命令

    \b
    使用示例：csp datatool eva img-cls -i '预测结果' -g '答案文件夹' -o '保存目录'
    """
    from csp.datatool.image_classify.eva import img_classify_eva
    if not os.path.isdir(gold_folder):
        raise FileNotFoundError("gold_folder should be a folder")
    try:
        img_classify_eva(submit_file, gold_folder, output=output)
    except Exception as ae:
        print(repr(ae))


## 二级命令
## 数据集统计分析 csp datatool eda
@datatool.group("eda")
def eda():
    """
    数据统计分析命令

    \b
    csp datatool eda 'commands' -h 获取子命令使用帮助
    """


## 三级命令
## 预测结果分析 csp datatool eda det-voc
@eda.command()
@click.option("-d", "--dataset", prompt="数据集目录", help="数据集目录", required=True)
@click.option("-o", "--output", prompt="统计分析结果保存目录", help="统计分析结果保存目录", required=True)
def det_voc(dataset, output):
    """
    目标检测任务VOC数据集统计分析命令

    \b
    使用示例：csp datatool eda det-voc -d '数据集目录' -o '保存目录'
    """
    from csp.datatool.image_detection.eda import det_eda
    try:
        det_eda(dataset, form="voc", output=output)
    except Exception as ae:
        print(repr(ae))


## 三级命令
## 预测结果分析 csp datatool eda det-coco
@eda.command()
@click.option("-d", "--dataset", prompt="数据集目录", help="数据集目录", required=True)
@click.option("-o", "--output", prompt="统计分析结果保存目录", help="统计分析结果保存目录", required=True)
def det_coco(dataset, output):
    """
    目标检测任务COCO数据集统计分析命令

    \b
    使用示例：csp datatool eda det-coco -d '数据集目录' -o '保存目录'
    """
    from csp.datatool.image_detection.eda import det_eda
    try:
        det_eda(dataset, form="coco", output=output)
    except Exception as ae:
        print(repr(ae))


## 三级命令
## 预测结果分析 csp datatool eda img-cls
@eda.command()
@click.option("-d", "--dataset", prompt="数据集目录", help="数据集目录", required=True)
@click.option("-o", "--output", prompt="统计分析结果保存目录", help="统计分析结果保存目录", required=True)
def img_cls(dataset, output):
    """
    图像分类任务平台数据集统计分析命令

    \b
    使用示例：csp datatool eda img-cls -d '数据集目录' -o '保存目录'
    """
    from csp.datatool.image_classify.eda import img_classify_eda
    try:
        img_classify_eda(dataset, output=output)
    except Exception as ae:
        print(repr(ae))


## 三级命令
## 预测结果分析 csp datatool eda text-entity
@eda.command()
@click.option("-d", "--dataset", prompt="数据集目录", help="数据集目录", required=True)
@click.option("-o", "--output", prompt="统计分析结果保存目录", help="统计分析结果保存目录", required=True)
def text_entity(dataset, output):
    """
    文本实体抽取分类任务平台数据集统计分析命令

    \b
    使用示例：csp datatool eda text-entity -d '数据集目录' -o '保存目录'
    """
    from csp.datatool.text_entity.eda import entity_eda
    try:
        entity_eda(dataset, output)
    except Exception as ae:
        print(repr(ae))


## 三级命令
## 预测结果分析 csp datatool eda text-entity-relation
@eda.command()
@click.option("-d", "--dataset", prompt="数据集目录", help="数据集目录", required=True)
@click.option("-o", "--output", prompt="统计分析结果保存目录", help="统计分析结果保存目录", required=True)
def text_entity_relation(dataset, output):
    """
    文本实体关系抽取任务平台数据集统计分析命令

    \b
    使用示例：csp datatool eda text-entity-relation -d '数据集目录' -o '保存目录'
    """
    from csp.datatool.text_entity_relation.eda import spo_eda
    try:
        spo_eda(dataset, output)
    except Exception as ae:
        print(repr(ae))


## 三级命令
## 预测结果分析 csp datatool eda text-cls
@eda.command()
@click.option("-d", "--dataset", prompt="数据集目录", help="数据集目录", required=True)
@click.option("-o", "--output", prompt="统计分析结果保存目录", help="统计分析结果保存目录", required=True)
def text_cls(dataset, output):
    """
    文本分类任务平台数据集统计分析命令

    \b
    使用示例：csp datatool eda text-cls -d '数据集目录' -o '保存目录'
    """
    from csp.datatool.text_classify.eda import text_classify_eda
    try:
        text_classify_eda(dataset, output)
    except Exception as ae:
        print(repr(ae))


## 二级命令
## VOC数据集增强 csp datatool aug
@datatool.group("aug")
def aug():
    """
    数据增强命令

    \b
    csp datatool aug 'commands' -h 获取子命令使用帮助
    """


## 三级命令
## VOC数据集增强 csp datatool aug det-voc
@aug.command()
@click.option("-d", "--dataset", prompt="数据集目录，支持VOC格式", help="数据集目录，支持VOC格式", required=True)
@click.option("-c", "--aug_file", prompt="增强配置yml文件", help="增强配置yml文件", required=True)
@click.option("-m", "--mode", type=click.Choice(['train', 'trainval']), help="增强依据，当同时存在train.txt、trainval.txt文件时，指定其一", default='trainval', required=True, show_default=True)
def det_voc(dataset, aug_file, mode):
    """
    目标检测任务VOC数据增强命令

    \b
    使用示例：csp datatool aug det-voc -d '数据集目录' -c 'aug.yaml' -m 'trainval'
    """
    from csp.datatool.image_detection.aug import det_aug
    try:
        det_aug(dataset, aug_file, mode)
    except Exception as ae:
        print(repr(ae))


## 三级命令
## VOC数据集增强 csp datatool aug img-cls
@aug.command()
@click.option("-d", "--dataset", prompt="数据集目录，支持平台格式数据集", help="数据集目录，支持平台格式数据集", required=True)
@click.option("-c", "--aug_file", prompt="增强配置yml文件", help="增强配置yml文件", required=True)
def img_cls(dataset, aug_file):
    """
    图像分类任务平台数据增强命令

    \b
    使用示例：csp datatool aug img-cls -d '数据集目录' -c 'aug.yaml'
    """
    from csp.datatool.image_classify.aug import img_classify_aug
    try:
        img_classify_aug(dataset, aug_file)
    except Exception as ae:
        print(repr(ae))


if __name__ == '__main__':
    print("start")
