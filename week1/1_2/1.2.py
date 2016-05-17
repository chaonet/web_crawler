#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup

# 获取网页并解析
soup = BeautifulSoup(open("index.html"), "lxml")
# print soup

# 图片列表
imgs = soup.select(".thumbnail > img")
# print imgs

# 价格列表
price_list = soup.select("div.caption > h4.pull-right")
# print price_list

# 标题列表
titles = soup.select("div.caption > h4 > a")
# print titles

# 评分数量列表
star_nums = soup.select("div.ratings > p.pull-right")
# print star_nums

# 星级列表
parents = soup.select("div.ratings")
# print parents
star_level_list = []

for parent in parents:
	star_level = parent.find_all("span", "glyphicon glyphicon-star")
	# print star_level
	# print len(star_level)
	star_level_list.append(len(star_level))

# 将每个商品的信息组成字典，放入列表，打印
goods = []

for title, img, price, star_num, star_level in zip(
		titles, imgs, price_list, star_nums, star_level_list):
	goods_info = {
		"title":title.get_text(),
		"img":img.get('src'),
		"price":price.get_text(),
		"star_num":star_num.get_text(),
		"star_level":star_level
	}

	goods.append(goods_info)

print goods
