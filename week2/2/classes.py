#!/usr/bin/env python
# coding: utf-8

import time

from bs4 import BeautifulSoup
import requests


def get_channel_list():
	channel_list = []
	url = "http://bj.ganji.com/wu/"
	web_data = requests.get(url)
	# print web_data.encoding
	# ISO-8859-1
	web_data.encoding = "utf-8"
	detail_soup = BeautifulSoup(web_data.text, 'lxml')
	class_list = detail_soup.select("dl.fenlei dt a")
	for i in class_list:
		# print i.get_text()
		# print i.get('href')
		channel_list.append("http://bj.ganji.com"+str(i.get('href')))

	# print channel_list

# get_channel_list()

# channel_list = ['http://bj.ganji.com/jiaju/', 'http://bj.ganji.com/rirongbaihuo/', 
# 			 'http://bj.ganji.com/shouji/', 'http://bj.ganji.com/shoujihaoma/', 
# 			 'http://bj.ganji.com/bangong/', 'http://bj.ganji.com/nongyongpin/', 
# 			 'http://bj.ganji.com/jiadian/', 'http://bj.ganji.com/ershoubijibendiannao/', 
# 			 'http://bj.ganji.com/ruanjiantushu/', 'http://bj.ganji.com/yingyouyunfu/', 
# 			 'http://bj.ganji.com/diannao/', 'http://bj.ganji.com/xianzhilipin/', 
# 			 'http://bj.ganji.com/fushixiaobaxuemao/', 'http://bj.ganji.com/meironghuazhuang/', 
# 			 'http://bj.ganji.com/shuma/', 'http://bj.ganji.com/laonianyongpin/', 
# 			 'http://bj.ganji.com/xuniwupin/', 'http://bj.ganji.com/qitawupin/', 
# 			 'http://bj.ganji.com/ershoufree/', 'http://bj.ganji.com/wupinjiaohuan/'
# 			]

channel_list = ['http://bj.ganji.com/jiaju/', 'http://bj.ganji.com/rirongbaihuo/',  
                'http://bj.ganji.com/bangong/', 'http://bj.ganji.com/nongyongpin/', 
                'http://bj.ganji.com/jiadian/', 'http://bj.ganji.com/ershoubijibendiannao/', 
                'http://bj.ganji.com/ruanjiantushu/', 'http://bj.ganji.com/yingyouyunfu/', 
                'http://bj.ganji.com/diannao/', 'http://bj.ganji.com/xianzhilipin/', 
                'http://bj.ganji.com/fushixiaobaxuemao/', 'http://bj.ganji.com/meironghuazhuang/', 
                'http://bj.ganji.com/shuma/', 'http://bj.ganji.com/laonianyongpin/', 
                'http://bj.ganji.com/xuniwupin/', 'http://bj.ganji.com/qitawupin/', 
                'http://bj.ganji.com/ershoufree/', 'http://bj.ganji.com/wupinjiaohuan/',
                'http://bj.ganji.com/shouji/',
               ]