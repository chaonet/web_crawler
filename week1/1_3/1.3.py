#!/usr/bin/env python
# coding: utf-8

import sys
import time
import math

from bs4 import BeautifulSoup
import requests

number = 0
detail_list = []

def detail_info(detail_urls):
    """每个详情页的信息"""
    global number, detail_list
    for i in detail_urls:
        number = number + 1

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
            'price':price[0].get_text(),
            'img_url':img[0]['data-bigimg'],
            'fangdong_img_url':fangdong_img[0].get('src'),
            'name':name[0].get_text(),
            'gender':gender_unicode
        }

        # detail_list.append(detail_dict)
        with open('result.txt','a') as f:
            f.write(str(detail_dict)+"\n")

        if number == 300:
            sys.exit(1)

def get_per_page_urls(url):
    """获取每一列表页的详情url列表"""
    detail_urls = []
    home_data = requests.get(url)
    soup = BeautifulSoup(home_data.text, 'lxml')
    detail_info_list = soup.select("#page_list > ul > li > a")
    for i in detail_info_list:
        detail_urls.append(i.get('href'))
    return detail_urls

def get_per_detail_num():
    """获取每一列表页详情url的数量"""
    url = "http://bj.xiaozhu.com/search-duanzufang-p1-0/"
    home_data = requests.get(url)
    soup = BeautifulSoup(home_data.text, 'lxml')
    count = len(soup.select("#page_list > ul > li"))
    return count

def url(num=300):
    """根据需要爬取的信息数量，计算需要请求的列表页url，返回列表页url列表"""
    # 需要爬取的页数
    # pages = num / get_per_detail_num() + 1
    pages = int(math.ceil(float(num)/get_per_detail_num()))
    list_urls = []

    for page in range(pages):
        url = "http://bj.xiaozhu.com/search-duanzufang-p{}-0/".format(page+1)
        list_urls.append(url)
    # print list_urls
    return list_urls

for i in url():
    # print i
    detail_urls = get_per_page_urls(i)
    # print detail_urls
    detail_info(detail_urls)
    print "%s 爬取完成" % i


