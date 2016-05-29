#!/usr/bin/env python
# coding: utf-8

import time

from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
bj58 = client['bj58']
info_links = bj58['links']

def get_links_url():

    for num in range(1,117):
        url = "http://bj.58.com/shoujihao/pn{}/".format(num)
        web_data = requests.get(url)
        time.sleep(1)
        detail_soup = BeautifulSoup(web_data.text, 'lxml')
        titles = detail_soup.select("strong.number")
        links = detail_soup.select("a.t")

        for title,link in zip(titles,links):
            data = {"title":title.get_text(), "link":link.get("href")}
            # print data
            info_links.insert_one(data)

        print "page %s 已完成"% num

get_links_url()
