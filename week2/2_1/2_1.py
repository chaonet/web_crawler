#!/usr/bin/env python
# coding: utf-8

import time

from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
xiaozhu = client['xiaozhu']
duanzhufang = xiaozhu['duanzhufang']

list_urls = ["http://bj.xiaozhu.com/search-duanzufang-p{}-0/".format(page) for page in range(1,4)]


def detail_info(detail_urls):
    """获取每个详情页的信息，保存到数据库"""

    for i in detail_urls:
        detail_data = requests.get(i)
        time.sleep(1)

        detail_soup = BeautifulSoup(detail_data.text, 'lxml')
        # print detail_soup

        title_list = detail_soup.select("div.pho_info > h4 > em")
        # print title_list[0].get_text()

        address = detail_soup.select("div.pho_info > p")
        # print address[0]['title']

        price = detail_soup.select("div.day_l > span")
        # print price[0].get_text()

        img = detail_soup.select("div.pho_show_r > div > ul.detail-thumb-nav > li > img")
        # print img[0]['data-bigimg']

        fangdong_img = detail_soup.select("div.js_box.clearfix > div.member_pic > a > img")
        # print fangdong_img[0].get('src')

        name = detail_soup.select("div.js_box.clearfix > div.w_240 > h6 > a")
        # print name[0].get_text()

        gender_str = detail_soup.select("div.js_box.clearfix > div.w_240 > h6 > span")
        gender = gender_str[0]['class'][0]
        if gender == 'member_girl_ico': 
            gender_unicode = u'女'
        else:
            gender_unicode = u'男'

        detail_dict = {
            'title':title_list[0].get_text(),
            'address':address[0]['title'],
            'price':int(price[0].get_text()),
            'img_url':img[0]['data-bigimg'],
            'fangdong_img_url':fangdong_img[0].get('src'),
            'name':name[0].get_text(),
            'gender':gender_unicode
        }

        # 保存结果到数据库
        duanzhufang.insert_one(detail_dict)


def get_per_page_urls(url):
    """获取每一列表页的详情url列表"""
    detail_urls = []
    home_data = requests.get(url)
    soup = BeautifulSoup(home_data.text, 'lxml')
    detail_info_list = soup.select("#page_list > ul > li > a")
    for i in detail_info_list:
        detail_urls.append(i.get('href'))
    return detail_urls


for url in list_urls:
    detail_urls = get_per_page_urls(url)
    # print url
    detail_info(detail_urls)
    print "%s 爬取完成" % url

# print duanzhufang.find({"price":{"$gte":500}})
# <pymongo.cursor.Cursor object at 0x103194f50>

print duanzhufang.find({"price":{"$gte":500}}).count()

