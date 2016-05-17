#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup

soup = BeautifulSoup(open("index.html"), "lxml")
# print soup

imgs = soup.select(".thumbnail > img")
# print imgs

for img in imgs:
	# print img.get('src')
	pass

price_list = soup.select("div.caption > h4.pull-right")
# print price_list

for price in price_list:
	# print price.get_text()
	pass

titles = soup.select("div.caption > h4 > a")
# print titles

for title in titles:
	# print title.get_text()
	pass

star_nums = soup.select("div.ratings > p.pull-right")
# print star_nums

for star_num in star_nums:
	# print star_num.get_text()
	pass

# stars = soup.select("div.ratings > p > span")
parents = soup.select("div.ratings")
# print parents
star_level_list = []

for parent in parents:
	star_level = parent.find_all("span", "glyphicon glyphicon-star")
	# print star_level
	# print len(star_level)
	star_level_list.append(len(star_level))

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
