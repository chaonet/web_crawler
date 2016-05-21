#!/usr/bin/env python
# coding: utf-8

import time

from bs4 import BeautifulSoup
import requests

infolist_url = "http://bj.58.com/pbdn/0/"

infolist_page = requests.get(infolist_url)
# print infolist_page

soup = BeautifulSoup(infolist_page.text, 'lxml')

detail_pages = soup.select("#infolist > table.tbimg > tr[logr] > td.img > a")


"""
单条测试
"""

# print detail_pages[1].get('href')

# detail_url = detail_pages[1].get('href')

# detail_page = requests.get(detail_url)

# detail_soup = BeautifulSoup(detail_page.text, 'lxml')

# class_info = detail_soup.select("span.crb_i > a")

# print class_info[1].get_text()

# title = detail_soup.select("div.col_sub.mainTitle > h1")

# print title[0].get_text()

# creat_time = detail_soup.select("li.time")

# print creat_time[0].get_text()

# price = detail_soup.select("span.price.c_f50")

# print price[0].get_text()

# visit = detail_soup.select("#totalcount")

# print visit[0].get_text() # TODO:

# quality = detail_soup.select("div.su_con > span")

# print (quality[1].string).strip()

# area = detail_soup.select("span.c_25d > a")

# # print area
# for i in area:
#     print i.get_text(),



for i in detail_pages[2:-1]:  # 第一条是推广，跳过
    """获取详细页面的信息"""

    print u"商品信息"

    detail_url = i.get('href')

    detail_page = requests.get(detail_url)

    detail_soup = BeautifulSoup(detail_page.text, 'lxml')

    class_info = detail_soup.select("span.crb_i > a")

    # print class_info,'class_info'

    print class_info[1].get_text()

    title = detail_soup.select("div.col_sub.mainTitle > h1")

    print title[0].get_text()

    creat_time = detail_soup.select("li.time")

    print creat_time[0].get_text()

    price = detail_soup.select("span.price.c_f50")

    print price[0].get_text()

    visit = detail_soup.select("#totalcount")

    print visit[0].get_text() # TODO: 未完成

    quality = detail_soup.select("div.su_con > span")

    print (quality[1].string).strip()

    area = detail_soup.select("span.c_25d > a")

    # print area
    for i in area:
        print i.get_text(),

    print
    print "="*20

    time.sleep(1)
