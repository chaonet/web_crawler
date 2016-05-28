#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.86 Safari/537.36',
}

proxies = {
    "http": "http://107.151.136.195:80/",
}

urls = ["http://weheartit.com/inspirations/taylorswift?page={}".format(i) for i in range(1, 21)]




"""测试用，抓取单个图片"""
# web_data = requests.get(urls[0])

# soup = BeautifulSoup(web_data.text, 'lxml')

# imgs = soup.select("img.entry_thumbnail")

# img_url = imgs[0].get("src")
# print img_url

# img_name = img_url.split('/')[4] + '.' + img_url.split('.')[-1]
# print img_name

# img_data = requests.get(img_url, proxies=proxies)
# print type(img_data.text)
# print type(img_data.content)
# print img_data.content

# with open(img_name, 'wb') as f:
#     # print type(img_data.content)
#     f.write(img_data.content)



for url in urls:
    web_data = requests.get(url)

    soup = BeautifulSoup(web_data.text, 'lxml')

    imgs = soup.select("img.entry_thumbnail")

    for i in imgs:
        img_url = i.get("src")
        print i.get("src")
        img_name = img_url.split('/')[4] + '.' + img_url.split('.')[-1]
        print img_name

        img_data = requests.get(img_url, headers=headers, proxies=proxies).content

        with open(img_name, 'wb') as f:
            print u"保存图片"
            # print type(img_data)
            f.write(img_data)


