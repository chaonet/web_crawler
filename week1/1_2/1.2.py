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

for i in range(len(titles)):
	goods_info = {}
	goods_info["title"] = titles[i].get_text()
	goods_info["img"] = imgs[i].get('src')
	goods_info["price"] = price_list[i].get_text()
	goods_info["star_num"] = star_nums[i].get_text()
	goods_info["star_level"] = star_level_list[i]

	goods.append(goods_info)

print goods
