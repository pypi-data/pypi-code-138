#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import argparse
import requests
from readability import Document
import tempfile
import uuid
import subprocess as subp
import re
import os
import json
import yaml
from urllib.parse import quote_plus
from os import path
from pyquery import PyQuery as pq
from datetime import datetime
from collections import OrderedDict
from EpubCrawler.img import process_img
from EpubCrawler.util import safe_mkdir
from . import __version__

DIR = path.dirname(path.abspath(__file__))

default_hdrs = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
}

RE_YAML_META = r'<!--yml([\s\S]+?)-->'
RE_TITLE = r'^#+ (.+?)$'
RE_CODE_BLOCK = r'```[\s\S]+?```'
RE_IMG = r'!\[.*?\]\(.*?\)'
# Word 字数统计标准：
# 一个汉字或中文标点算一个字
# 一个连续的英文字母、标点和数字序列算一个字
RE_ZH_WORD = r'[\u2018-\u201d\u3001-\u301c\u4e00-\u9fff\uff01-\uff65]'
RE_EN_WORD = r'[\x21-\x7e]+'

def d(name):
    return path.join(DIR, name)

def tomd(html):
    js_fname = d('tomd.js')
    html_fname = path.join(tempfile.gettempdir(), uuid.uuid4().hex + '.html')
    open(html_fname, 'w', encoding='utf8').write(html)
    subp.Popen(
        ["node", js_fname, html_fname],
        shell=True,
    ).communicate()
    md_fname = re.sub(r'\.html$', '', html_fname) + '.md'
    md = open(md_fname, encoding='utf8').read()
    os.remove(html_fname)
    return md

def fname_escape(name):
    return name.replace('\\', '＼') \
               .replace('/', '／') \
               .replace(':', '：') \
               .replace('*', '＊') \
               .replace('?', '？') \
               .replace('"', '＂') \
               .replace('<', '＜') \
               .replace('>', '＞') \
               .replace('|', '｜')

def account_handle(args):
    if not args.file.endswith('.md'):
        print('请提供 markdown 文件')
        return
    print(args.file)
    cont = open(args.file, encoding='utf8').read()
    # 去掉代码块和图片
    cont = re.sub(RE_CODE_BLOCK, '', cont)
    cont = re.sub(RE_IMG, '', cont)
    zh_count = len(re.findall(RE_ZH_WORD, cont))
    en_count = len(re.findall(RE_EN_WORD, cont))
    total = zh_count + en_count
    print(f'中文字数：{zh_count}\n英文字数：{en_count}\n总字数：{total}')

def fix_handle(args):
    if not args.file.endswith('.md'):
        print('请提供 markdown 文件')
        return
    cont = open(args.file, encoding='utf8').read()
    dir = path.dirname(args.file)
    rm = re.search(RE_TITLE, cont, flags=re.M)
    if not rm: 
        print(f'{args.file} 未找到标题')
        return
    title = rm.group(1)
    nfname = re.sub(r'\s', '-', fname_escape(title)) + '.md'
    nfname = path.join(dir, nfname)
    print(nfname)
    os.rename(args.file, nfname)

def download_handle(args):
    html = requests.get(
        args.url,
        headers=default_hdrs,
    ).content.decode(args.encoding, 'ignore')
    
    # 解析标题
    rt = pq(html)
    el_title = rt.find('title').eq(0)
    title = el_title.text().strip()
    el_title.remove()
    
    # 判断是否重复
    title_esc = re.sub(r'\s', '-', fname_escape(title))
    fname = f'docs/{title_esc}.md'
    if path.isfile(fname):
        print(f'{title} 已存在')
        return
    
    # 解析内容并下载图片
    co = Document(str(rt)).summary()
    co = pq(co).find('body').html()
    imgs = {}
    co = process_img(co, imgs, img_prefix='img/', page_url=args.url)
    html = f'''
    <html><body>
    <h1>{title}</h1>
    <blockquote>
    来源：<a href='{args.url}'>{args.url}</a>
    </blockquote>
    {co}</body></html>
    '''
    
    # 转换 md
    md = tomd(html)
    # md = re.sub(RE_CODE_BLOCK, code_replace_func, md)
    yaml_head = '\n'.join([
        '<!--yml',
        'category: ' + args.category,
        'date: ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        '-->',
    ])
    md = f'{yaml_head}\n\n{md}'
    
    # 写入硬盘
    safe_mkdir('docs')
    safe_mkdir('docs/img')
    open(fname, 'w', encoding='utf-8').write(md)
    for name, data in imgs.items():
        open(f'docs/img/{name}', 'wb').write(data)
        
    print('已完成')
    
def summary_handle(args):
    # 读入文件列表
    fnames = [f for f in os.listdir('docs') if f.endswith('.md')]
    toc = OrderedDict()
    for fname in fnames:
        print(fname)
        md = open(path.join('docs', fname), encoding='utf8').read()
        # 提取元信息
        m = re.search(RE_YAML_META, md)
        if not m: 
            print('未找到元信息，已跳过')
            continue
        try:
            meta = yaml.safe_load(m.group(1))
        except Exception as ex: 
            print(ex)
            continue
        dt = meta.get('date', '0001-01-01 00:00:00')
        cate = meta.get('category', '未分类')
        # 提取标题
        m = re.search(RE_TITLE, md, flags=re.M)
        if not m: 
            print('未找到标题，已跳过')
            continue
        title = m.group(1)
        toc.setdefault(cate, [])
        toc[cate].append({
            'title': title,
            'file': fname,
            'date': dt,
        })
    
    # 生成目录文件
    summary = ''
    for cate, sub in toc.items():
        summary += f'+   {cate}\n'
        for art in sub:
            title = art['title']
            file = quote_plus(art['file'])
            summary += f'    +   [{title}](docs/{file})\n'
    open('SUMMARY.md', 'w', encoding='utf8').write(summary)
    
def main():
    parser = argparse.ArgumentParser(prog="BookerWikiTool", description="iBooker WIKI tool", formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-v", "--version", action="version", version=f"BookerWikiTool version: {__version__}")
    parser.set_defaults(func=lambda x: parser.print_help())
    subparsers = parser.add_subparsers()
    
    dl_parser = subparsers.add_parser("download", help="download a page")
    dl_parser.add_argument("url", help="url")
    dl_parser.add_argument("-e", "--encoding", default='utf-8', help="encoding")
    dl_parser.add_argument("-c", "--category", default='未分类', help="category")
    dl_parser.set_defaults(func=download_handle)
    
    sum_parser = subparsers.add_parser("summary", help="generate the summary")
    sum_parser.set_defaults(func=summary_handle)
    
    fix_parser = subparsers.add_parser("fix", help="fix titles")
    fix_parser.add_argument("file", help="file")
    fix_parser.set_defaults(func=fix_handle)
    
    acc_parser = subparsers.add_parser("account", help="account words")
    acc_parser.add_argument("file", help="file")
    acc_parser.set_defaults(func=account_handle)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__": main()