#!/usr/bin/env python
# coding: utf-8

import time

from bs4 import BeautifulSoup
import requests


def get_views(detail_url):
    """获取指定页面的浏览量"""

    infoid = detail_url.split("?")[0].split("/")[-1].strip("x.shtml")

    views_url = "http://jst1.58.com/counter?infoid={}".format(infoid)
    # print views_url

    headers = {
        "Host":"jst1.58.com",
        "Connection":"keep-alive",
        "Cache-Control":"max-age=0",
        "Accept":"*/*",
        "User-Agent": r"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
        "Referer": detail_url,
        "Accept-Encoding":"gzip, deflate, sdch",
        "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
        "Cookie":r'id58=c5/njVc+c4tUnwgiDMtjAg==; bj58_id58s="UU16Wm1FaFgrUnpMNDA4Mg=="; sessionid=d030f6af-5efe-4c6c-84c7-c9e4649a2da0; als=0; myfeet_tooltip=end; 58home=suqian; bangbigtip2=1; ipcity=suqian%7C%u5BBF%u8FC1; 58tj_uuid=3e53804a-394e-47a3-8047-893ea4c56f92; new_session=0; new_uv=7; utm_source=; spm=; init_refer=http%253A%252F%252Fbj.58.com%252Fpbdn%252F0%252F; final_history=26054432868687%2C26080615630506%2C26045484799931; bj58_new_session=0; bj58_init_refer="http://bj.58.com/pbdn/0/"; bj58_new_uv=7',
    }

    views = requests.get(views_url, headers=headers).text.split("=")[2]

    # print views
    return views


def get_detail_url(pages, source):
    """获取需要爬取的详细商品url"""

    urls = []

    for i in range(pages):
        infolist_url = "http://bj.58.com/pbdn/{source}/pn{page}".format(source=source, page=i+1)

        infolist_page = requests.get(infolist_url)
        time.sleep(1)
        # print infolist_page

        soup = BeautifulSoup(infolist_page.text, 'lxml')

        detail_pages = soup.select("#infolist > table.tbimg > tr[logr] > td.img > a")

        urls = [i.get('href') for i in detail_pages] # 第一条是推广，跳过

    # print urls
    return urls[2:-1]


def get_detail_info(page=1, source=0):
    """获取详细页面的信息"""

    urls = get_detail_url(page, source)

    for i in urls:

        print u"商品信息"

        detail_page = requests.get(i)
        time.sleep(1)

        detail_soup = BeautifulSoup(detail_page.text, 'lxml')

        class_info = detail_soup.select("span.crb_i > a")[1].get_text()
        print class_info

        title = detail_soup.select("div.col_sub.mainTitle > h1")[0].get_text()
        print title

        creat_time = detail_soup.select(".time")[0].get_text()
        print creat_time

        price = detail_soup.select(".c_f50")[0].get_text()
        print price

        quality = detail_soup.select(".su_con > span")
        print (quality[1].string).strip()

        views = get_views(i)
        print views

        area_data = detail_soup.select("span.c_25d")
        area =  list(area_data[0].stripped_strings) if area_data else None
        print area

        print "="*20


# get_detail_url()

get_detail_info(page=1, source=0)


