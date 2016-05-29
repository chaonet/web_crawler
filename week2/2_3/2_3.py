#!/usr/bin/env python
# coding: utf-8

import time

from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
bj58 = client['bj58']
info_links = bj58['links']
detailinfo = bj58['detailinfo']


def get_links_url():
    """获取列表页中所有详情页的标题和链接"""
    for num in range(1,117):
        url = "http://bj.58.com/shoujihao/pn{}/".format(num)
        web_data = requests.get(url)
        time.sleep(1)
        detail_soup = BeautifulSoup(web_data.text, 'lxml')
        if num == 1:
            boxlist = detail_soup.select("div.boxlist div.boxlist")[1]
        else:
            boxlist = detail_soup.select("div.boxlist div.boxlist")[0]
        titles = boxlist.select("strong.number")
        links = boxlist.select("a.t")

        for title,link in zip(titles,links):
            data = {"title":title.get_text(), "link":link.get("href")}
            # print data
            info_links.insert_one(data)

        print "page %s 已完成"% num

# get_links_url()


def get_item_info():
    """获取详情页url，抓取详情信息"""

    # url 列表
    url_lists = [item['link'] for item in info_links.find()]
    if detailinfo.find().count() > 0:  # 判断是否中断过
        item_lists = [item['url'] for item in detailinfo.find()]
        url_lists = set(url_lists)-set(item_lists)  # 获取未爬取的 url 子集

    for url in url_lists:
        item_data = requests.get(url)
        detail_soup = BeautifulSoup(item_data.text, 'lxml')

        number = list(detail_soup.select("h1")[0].stripped_strings)[0]
        info_list = number.replace('\t','').replace(' ',"").replace('\n\n\n','\n').split("\n")
        # print 'number= ',info_list[0]
        # print 'isp= ', info_list[1]

        price = list(detail_soup.select(".price")[0].stripped_strings)[0].split(' ')[0]
        # print 'price= ', price

        seller = detail_soup.select(".vcard a.tx")[0].get_text()
        # print seller

        telephon = list(detail_soup.select(".arial")[0].stripped_strings)[0]
        # print tele

        data = {"sell_number": info_list[0],
                "isp": info_list[1],
                "price": price,
                "seller": seller,
                "telephon": telephon,
                "url": url
               }

        detailinfo.insert_one(data)
        print "%s 已完成"% str(url)


get_item_info()
