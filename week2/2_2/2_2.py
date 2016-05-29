#!/usr/bin/env python
# coding: utf-8

import time

from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
bj58 = client['bj58']
info_links = bj58['links']
info_detail = bj58['detailinfo']


"""单列表页测试"""
# url = "http://bj.58.com/shoujihao/pn2/"
# web_data = requests.get(url)
# detail_soup = BeautifulSoup(web_data.text, 'lxml')
# boxlist = detail_soup.select("div.boxlist div.boxlist")[1]
# print boxlist


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


"""单详情页测试"""
# links_data = info_links.find()
# url = links_data[0]['link']
# url = "http://short.58.com/zd_p/2e7875cf-cdd8-4eaa-baaf-1ac1b111e6d8/?target=dc-16-xgk_fegvcjemg_39429002744563q-feykn&end=end26096779100482x.shtml&psid=169068509191954188512724262&entinfo=26096779100482_0"
# url = "http://bj.58.com/shoujihao/26174847169485x.shtml?psid=110931214191953798800116449&entinfo=26174847169485_0&iuType=p_2&PGTID=0d3000f1-0000-18cd-243b-e75642b75928&ClickID=1"
# item_data = requests.get(url)
# detail_soup = BeautifulSoup(item_data.text, 'lxml')
# number = list(detail_soup.select("h1")[0].stripped_strings)[0]

# info_list = number.replace('\t','').replace(' ',"").replace('\n\n\n','\n').split("\n")

# print 'number= ',info_list[0]
# print 'isp= ', info_list[1]

# price = list(detail_soup.select(".price")[0].stripped_strings)[0].split(' ')[0]
# print 'price= ', price

# seller = detail_soup.select(".vcard a.tx")[0].get_text()
# print seller

# tele = list(detail_soup.select(".arial")[0].stripped_strings)[0]
# print tele


def get_item_info():
    """获取详情页url，抓取详情信息"""
    num = info_links.find().count()
    links_data = info_links.find()
    for i in range(num):
        url = links_data[i]['link']
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
               }

        info_detail.insert_one(data)
        print "%s 已完成"% str(url)


get_item_info()
