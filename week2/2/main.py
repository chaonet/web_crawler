#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Pool

from classes import channel_list
from item_info import get_links_from, get_item_detail_info, info_links, info_detail

db_urls = [item['url'] for item in info_links.find()]
item_urls = [item['url'] for item in info_detail.find()]
result_urls = set(db_urls) - set(item_urls)

# result_urls = [item['url'] for item in info_links.find()]

def get_all_links_from(channel):
    for num in range(1,117):
        get_links_from(channel, num)

# def get_item_detail(item):
#     get_item_detail_info(item['link'])

# urls = [item['link'] for item in info_links.find()]

if __name__ == "__main__":
    pool = Pool()
    # pool.map(get_all_links_from, channel_list)
    pool.map(get_item_detail_info, result_urls)

# map(lambda x:x+1,iter(range(100000)))