#!/usr/bin/env python
# coding: utf-8

import time

from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient

client = MongoClient('localhost', 27017, connect=False)
ganji = client['ganji']
info_links = ganji['links']
info_detail = ganji['detailinfo']

headers = {'Accept':'*/*',
           'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
           'Connection':'keep-alive',
           'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36}',
          }



def get_links_from(classes,num=1):
    """获取列表页中，详情页的url，并存储"""
    # url_list = []
    url = '{}o{}/'.format(classes, num)
    print url
    web_data = requests.get(url, headers=headers)
    detail_soup = BeautifulSoup(web_data.text, 'lxml')
    if detail_soup.find("ul","pageLink"):
        # print 1
        # print detail_soup
        if detail_soup.find("a","ft-tit"):
            # print 3
            item_list = detail_soup.select(".ft-tit")
        else:
            # print 4
            item_list = detail_soup.select(".infor-title01")
        # print item_list
        # item_list = detail_soup.select("a.ft-tit")
        for item in item_list:
            url = item.get('href')
            if 'm.zhuanzhuan.58.com' in url:
                pass
            else:
                print url
                # info_links.insert_one({'url': url})
    else:
        # print 2
        pass

# get_links_from(channel_list[18])
# http://bj.ganji.com/ershoubijibendiannao/
# http://bj.ganji.com/shoujihaoma/o1/
# get_links_from("http://bj.ganji.com/qitawupin/")

# url = 'http://bj.ganji.com/jiaju/o1/'
# web_data = requests.get(url)
# detail_soup = BeautifulSoup(web_data.text, 'lxml')
# item_list = detail_soup.select(".ft-tit")[0].get('href')
# print item_list


def get_item_detail_info(url):
    """获取每个详情页中的数据，并存储"""
    # url = "http://biz.click.ganji.com/bizClick?url=pZwY0jCfsvFJshI6UhGGshPfUiqJpy7JIitQPj0dPHnLP1DvXaOCIAd0njTQrNFAE1u7wWKAnDNLnjIDP1bdnHcOEYmYEWKjwjc1E160njTQPHbdPjNzn1EYrjEQnWm3rj0zPH03PRkknjDVgjTknHc3PH9zPWn1PdkknjDQP7kknjDQPj0dPHnLP1DvgjTknHD1r7kknjDQn1w0njTQnHE3gjTknHDzgjTknHDYPWEdnWEzPjE1PHR0njTQnRkknjDQn170njTQmh-buA-8udkknjDQgjTknHDOnj0vnj9Yg1wx0AI0njTQn7kknjDdrHNYPHc1PjE3PjDzPW93P1cdP19dgjTknHK0njTQPjb8rjb8nWm8nWTOgjTknNdfXh-_UADfPi3kca6PmyPGUMwf0v9ecD-8IAR_cDd6mzK5NzKmcjDkg1Dkg1NGcD7k0AQ-RvRBiv-Ys1N1Pz31PBTCiY6NHNk_cAQGpvN9wvRWpvtGcDPC0hqVuitdna3ksWcvPWD8nHTzc7P6uh7zpitdn108n1u0njTQPH9YgjTkniYQgjTkniYQgjTknNPC0hqVuRkknj7bPAPBrAEOuiYvPHDOsHEvnjDVrHT3riYOnHcdm193uj7WPHb&v=2"
    print url
    # url = "http://m.zhuanzhuan.58.com/Mzhuanzhuan/zzWebInfo/zzganji/zzpc/detailPc.html?infoId=736841308648177667&cateId=107&fullCate=107&fullLocal=1&zzfrom=ganjiweb&zhuanzhuanSourceFrom=722"
    web_data = requests.get(url, headers=headers)
    time.sleep(2)
    web_data.encoding = "utf-8"
    detail_soup = BeautifulSoup(web_data.text, 'lxml')
    # print detail_soup
    if detail_soup.find("body", "b-detail"):  # 如果还没有下架
        print "begin"
        title = detail_soup.select(".title-name")[0].get_text()
        # print title
        date_exist = detail_soup.select(".title-info-l.clearfix li i")[0]
        # print list(date_exist.get_text())
        # [u'\n', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u'0', u'5', u'-', u'2', u'9', u'\xa0', u'\u53d1', u'\u5e03', u'\xa0', u'\xa0', u'\xa0', u'\xa0', u'\xa0', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ', u' ']
        
        # print date_exist.get('class')[0]
        # pr-5
        
        if date_exist.get('class')[0] == "pr-5":
            # date = date_exist.get_text().lstrip('\n').lstrip(' ').split(u'\xa0')[0]
            date = date_exist.get_text().strip().split(u'\xa0')[0]
        else:
            date = None
        # print date
        goods_type = detail_soup.select(".det-infor a")[0].get_text()
        # print goods_type
        if detail_soup.find('i','f22'):
            price = int(detail_soup.select(".f22")[0].get_text())
            # print price
        else:
            price = 0

        location = list(map(lambda x:x.text,detail_soup.select('ul.det-infor > li:nth-of-type(3) > a')))
        # 位置可能不止两个元素
        #wrapper > div.content.clearfix > div.leftBox > div:nth-child(3) > div > ul > li:nth-child(3)
        # print location[0], location[1]
        # location = list(detail_soup.select(".det-infor li")[2].stripped_strings)
        # print location[1], location[3]
        if detail_soup.find("ul", "second-det-infor"):
            condition_list = list(detail_soup.select(".second-det-infor.clearfix li")[0].stripped_strings)
            condition = condition_list[1].split('，'.decode("utf-8"))[0]
        else:
            condition = None
        # print condition

        data = {'title': title,
                'date': date,
                'goods_type': goods_type,
                'price': price,
                'location': location,
                'condition': condition,
                'url': url
               }

        # print data
        info_detail.insert_one(data)

    else:
        print "False"
        pass
    # [location[1], location[3]]

# get_item_detail_info("http://biz.click.ganji.com/bizClick?url=pZwY0jCfsvFJshI6UhGGshPfUiqBmyOMUvOMs1DOnHEYPHmvPjF3sh6YURkknj77PWEOnbPKPW-KnWNQwHcLE1KDwDPKEWmvPbu7rjb1n-kknj70njTQsRkknjDQnWc3P1mQPWu0njTQnHw0njTQnHbQPjEdPWmYn-kknjDvn7kknjDdndkknjDQPj60njTQnHF0njTQnHEvPjmkPHnLrH0YPRkknjDzn7kknjDQn170njTQmh-buA-8udkknjDQgjTknyI6UhGGmvqVgLKMgjTknHK0njTQgjTknHK0njTQnHDzsWc1sWc8P1K0njTQHyqlpyQ_mitdsWT92Dd6mv-8IAq1pj_9iyOYuyk9Hy7WcDqHc799nHKxnHKxPib9EgKkUARguyFspgEfPHnLsWnvca6si7wPHak9UA-ouiKZuyPoUzb9Ev6zUvd-s1NksWT8nWmvni3Qnjc9Nv7hmgFGs1N1Pz31PMd0njTQPH9YgjTkniYQgjTkniYQgjTknNPC0hqVuRkknj7WmyDknvu6niY3P176sHwbnynVmhuhmBY1PHmzrjbdrAN3nHD&v=2")
# get_item_detail_info("http://bj.ganji.com/jiaju/2091058746x.htm")

# get_item_detail_info("http://biz.click.ganji.com/bizClick?url=pZwY0jCfsvFJshI6UhGGshPfUiqzpgFfUhIBmy-CIytfnWTOrHNLnH0LrZ98pZwVgjTknHEQn1Edwj-DwNcYwDFjEHDkPW0vn1FDrjI7EN7Dn101gjTknHNOPHEdnWnYPj9YnHcvrj9LnWNLrjR0njTQsRkknjDYrHnknjmknWK0njTQnHw0njTQnWTOrHNLnH0Lr7kknjDLn7kknjDdPRkknjDQn1EvgjTknHDzgjTknHDYPWEvnWTvnHDdPju0njTQnRkknjDQn170njTQmh-buA-8udkknjDQgjTknHDOnj0vnj9Yg1ux0AI0njTQn7kknjDdrHNYPHc1PjE3PjDzPW93P1cdP19dgjTknHK0njTQPjb8rjb8nWm8nWTOgjTknNdfXh-_UADfPi3kca6PmyPGUMwf0v9ecD-8IAR_cDd6mzK5NzKmcjDkg1Dkg1NGcD7k0AQ-RvRBiv-Ys1N1Pz31PBTCiY6NHNk_cAQGpvN9wvRWpvtGcDPC0hqVuitdna3ksWcvPWD8nHTzc7P6uh7zpitdn108n1u0njTQPH9dgjTkniYQgjTkniYQgjTknNPC0hqVuRkknjDzP1FWPjuBmiYYnyNzsHE3PWNVrjbOnBYQPhNdnvDduW9QnW0&v=2")
# get_item_detail_info("http://biz.click.ganji.com/bizClick?url=pZwY0jCfsvFJshI6UhGGshPfUiqJpy7JIitQPj0dPHnLP1DvXaOCIAd0njTQEHw7nWcznjTdPWNLnbDYEbc1ENm3PjTQEH9YwHKKnNw0njTQPHbdPjNzn1EYrjEQnWm3rj0zPH03PRkknjDVgjTknHc3PH9zPWn1PdkknjDQP7kknjDQPj0dPHnLP1DvgjTknHDQr7kknjDQnHR0njTQnHE3gjTknHDzgjTknHDYPWEvnWTLP1TdP1-0njTQnRkknjDQn170njTQmh-buA-8udkknjDQgjTknHDOnj0vnj9Yg1ux0AI0njTQn7kknjDdrHNYPHc1PjE3PjDzPW93P1cdP19dgjTknHK0njTQPjb8rjb8nWm8nWTOgjTknNdfXh-_UADfPi3kca6PmyPGUMwf0v9ecD-8IAR_cDd6mzK5NzKmcjDkg1Dkg1NGcD7k0AQ-RvRBiv-Ys1N1Pz31PBTCiY6NHNk_cAQGpvN9wvRWpvtGcDPC0hqVuitdna3ksWcvPWD8nHTzc7P6uh7zpitdn108n1u0njTQPH9YgjTkniYQgjTkniYQgjTknNPC0hqVuRkknjDdnyELuhcknBYduAuhsHw-mWNVrANdmBdBPWDkrjT1mW91PAN&v=2")
# get_item_detail_info("http://biz.click.ganji.com/bizClick?url=pZwY0jCfsvFJshI6UhGGshPfUiq1pAqdphbfnWDYPjnYrjnvrZ98pZwVgjTknH-7EbDLPNRarHcOwW0drHndPYNYP1TQENRAnNnYEWTzgjTknHNOPHEdnWnYPj9YnHcvrj9LnWNLrjR0njTQsRkknjDvPjbYrHEQnH60njTQnHw0njTQnWDYPjnYrjnvr7kknjDQrjK0njTQnHn1gjTknHD1PRkknjDQn-kknjDQPjmYPWckrjcdPjDQgjTknH70njTQnHnQgjTknyFGuAwGUhI0njTQnRkknj7MmyOJpyPfURqkudkknjDkgjTknHNOPHEdnWnYPj9YnHcvrj9LnWNLrjR0njTQn7kknjDYri33ri3zPB3znj-0njTQHyqlpyQ_mitdsWT92Dd6mv-8IAq1pj_9iyOYuyk9Hy7WcDqHc799nHKxnHKxPib9EgKkUARguyFspgEfPHnLsWnvca6si7wPHak9UA-ouiKZuyPoUzb9Ev6zUvd-s1NksWT8nWmvni3Qnjc9Nv7hmgFGs1N1Pz31P-kknjDdrjI0njTQsH70njTQsH70njTQEv6zUvd-gjTknHT1mHRbmhRWsHmYPvDVPjPhnzYOuAcdsH6hP1w-P1KWrHNvnE&v=2")
# get_item_detail_info("http://biz.click.ganji.com/bizClick?url=pZwY0jCfsLPCshI6UhGGshPfUiqBmyOMUvOMs1DLrj9QrHDdPW63sh6YURkknjDzwjELEWbLPHbkrHIAPHc3rNwKrHN1PYPDP16Anjn3wRkknjDdrHNYPHc1PjE3PjDzPW93P1cdP19dgjTknid0njTQnWE1nHNkPH9OgjTknHDYgjTknHDLrj9QrHDdPW60njTQPHTkgjTknHNkn7kknjDQPjR0njTQnHF0njTQnHEvPjmznj9vPW0QPdkknjDQgjTknHD1nRkknj7BpywbpyOMgjTknH70njTQnHbkP1mkrjwxr7qkudkknjDkgjTknHNOPHEdnWnYPj9YnHcvrj9LnWNLrjR0njTQn7kknjDYri33ri3zPB3znj-0njTQHyqlpyQ_mitdsWT92Dd6mv-8IAq1pj_9iyOYuyk9Hy7WcDqHc799nHKxnHKxPib9EgKkUARguyFspgEfPHnLsWnvca6si7wPHak9UA-ouiKZuyPoUzb9Ev6zUvd-s1NksWT8nWmvni3Qnjc9Nv7hmgFGs1N1Pz31P-kknjDdrHK0njTQsH70njTQsH70njTQEv6zUvd-gjTknH6WPjIWuHPbsHbLmWcVPANQPzYOPjEvsH6bryw-PywbPvF-PE&v=2")
# get_item_detail_info("http://bj.ganji.com/nongyongpin/1472586682x.htm")
# get_item_detail_info("http://biz.click.ganji.com/bizClick?url=pZwY0jCfsvFJshI6UhGGshPfUiqJpy7bpy78s1cknjbkPjbkPjF3sh6YURkknjDvnNPKP1T1rNcLPHu7wbndwWDQP1ndP1DdnjnQPbDkw7kknjDdrHNYPHc1PjE3PjDzPW93P1cdP19dgjTknid0njTQnWnQrHDQrjbOgjTknHDYgjTknHcknjbkPjbkPjF0njTQnHnkgjTknHD1n7kknjDQn1I0njTQnHF0njTQnHEvPjmznHTOPH93rRkknjDQgjTknHD1nRkknj7BpywbpyOMgjTknH70njTQuv78ph-WUvdx0AI0njTQn7kknjDdrHNYPHc1PjE3PjDzPW93P1cdP19dgjTknHK0njTQPjb8rjb8nWm8nWTOgjTknNdfXh-_UADfPi3kca6PmyPGUMwf0v9ecD-8IAR_cDd6mzK5NzKmcjDkg1Dkg1NGcD7k0AQ-RvRBiv-Ys1N1Pz31PBTCiY6NHNk_cAQGpvN9wvRWpvtGcDPC0hqVuitdna3ksWcvPWD8nHTzc7P6uh7zpitdn108n1u0njTQPH91gjTkniYQgjTkniYQgjTknNPC0hqVuRkknjDvmWnzujcduiYknAcksHEvmvcVmHcLnzdWnHI-nvmYnWN1rjc&v=2")
# get_item_detail_info("http://biz.click.ganji.com/bizClick?url=pZwY0jCfsvFJshI6UhGGshPfUiq-0MPCULRBpyGGmhR8uA-6UhO6UztznjbkP1mvPHc3XaOCIAd0njTQnDRAP1EQnDnOPNDkENFKwbFKnW-DPNNYnYmzwjD1PWu0njTQPHbdPjNzn1EYrjEQnWm3rj0zPH03PRkknjDVgjTknHEYnWc1PjmYn-kknjDQP7kknjDznjbkP1mvPHc3gjTknHDkn7kknjDdn7kknjDQn1w0njTQnHF0njTQnHEvPjmznHDYP1E3P7kknjDQgjTknHD1nRkknj7BpywbpyOMgjTknH70njTQnHbkP1mkrjwxr7qkudkknjDkgjTknHNOPHEdnWnYPj9YnHcvrj9LnWNLrjR0njTQn7kknjDYri33ri3zPB3znj-0njTQHyqlpyQ_mitdsWT92Dd6mv-8IAq1pj_9iyOYuyk9Hy7WcDqHc799nHKxnHKxPib9EgKkUARguyFspgEfPHnLsWnvca6si7wPHak9UA-ouiKZuyPoUzb9Ev6zUvd-s1NksWT8nWmvni3Qnjc9Nv7hmgFGs1N1Pz31P-kknjDvrH60njTQsH70njTQsH70njTQEv6zUvd-gjTknHn1mW7WmhcLsH7-PhNVPAuBnzdBn1uWsHmQmW0vnhNQuj66rT&v=2")
# get_item_detail_info("http://biz.click.ganji.com/bizClick?url=pZwY0jCfsvFJshI6UhGGshPfUiqzIy78ph-6UMwd0v6ds1DOPWELnjmLPW-3sh6YURkknj77Eb7DEH9YnHbLnDn3nYFKPbnQPDc3PDu7PYm3wD7Ar7kknjDdrHNYPHc1PjE3PjDzPW93P1cdP19dgjTknid0njTQnWTLPWE1ndkknjDQP7kknjDQrHmYP1TvP1mOgjTknHnzn7kknjD1nH-0njTQnHnOgjTknHDzgjTknHDYPWEvnWDQrjczP1P0njTQnRkknjDQn170njTQmh-buA-8udkknjDQgjTknHDOnj0vnj9Yg16x0AI0njTQn7kknjDdrHNYPHc1PjE3PjDzPW93P1cdP19dgjTknHK0njTQPjb8rjb8nWm8nWTOgjTknNdfXh-_UADfPi3kca6PmyPGUMwf0v9ecD-8IAR_cDd6mzK5NzKmcjDkg1Dkg1NGcD7k0AQ-RvRBiv-Ys1N1Pz31PBTCiY6NHNk_cAQGpvN9wvRWpvtGcDPC0hqVuitdna3ksWcvPWD8nHTzc7P6uh7zpitdn108n1u0njTQPHbLgjTkniYQgjTkniYQgjTknNPC0hqVuRkknjDvnH6BnvEduid6PvnksHw-nvDVrAPhmiYzmWKbrHTknjmOrAD&v=2")
# get_item_detail_info("http://bj.ganji.com/yingyouyunfu/2153528138x.htm")
# get_item_detail_info("http://bj.ganji.com/diannao/2142642894x.htm")
# get_item_detail_info("http://biz.click.ganji.com/bizClick?url=pZwY0jCfsvFJshI6UhGGshPfUiqhIgPCpg6GmyqBmg6duyd6UztznHN1PjcOrH9YXaOCIAd0njTQnYc3wH9zwDnvnj0vnWNdrHIDPH01EWmzEW9zPWnYrHP0njTQPHbdPjNzn1EYrjEQnWm3rj0zPH03PRkknjDVgjTknHcdn1DvP1bdnRkknjDQP7kknjDznHN1PjcOrH9YgjTknHNkgjTknHnvgjTknHc3r7kknjDQn-kknjDQPjmYPWcQn1T3nWmdgjTknH70njTQnHnQgjTknyFGuAwGUhI0njTQnRkknjDQrHTLPWT3P7tvgLKMgjTknHK0njTQPHbdPjNzn1EYrjEQnWm3rj0zPH03PRkknjDkgjTknHEOsW9OsWcvsWckrRkknj7PULGGUAQ6s1N8naTCHy7WpyOYULPCrzKFUMw-UaKPmyn9Hdn9yaTQn7tQn7td2iKK0ZK_uRI-mbVGIatdn108n1m92DVcRDdnsaK_pyV-cDI-mvVf2iKjpZFfUyNfPHT8na3zPWmQsWDknBKHmyu60hbfPHnLsWnvgjTknHmkn7kknjDVnRkknjDVnRkknj7jpZFfUyR0njTQPhNkmvPBmhNVnhN3PzYYmHndsy7hPymVPvnQnj7-nANzPhmv&v=2")
# get_item_detail_info("http://biz.click.ganji.com/bizClick?url=pZwY0jCfsvFJshI6UhGGshPfUiqhIgPCpg6GmyqBmg6duyd6UztznHN1PjcOrH9YXaOCIAd0njTQwWm3nYRDrjc3PjndnHFArHbOwWDknjmOnj0krNE3EW-0njTQPHbdPjNzn1EYrjEQnWm3rj0zPH03PRkknjDVgjTknHcdn1DvP1bdnRkknjDQP7kknjDznHN1PjcOrH9YgjTknHDkP-kknjDLPdkknjDQPjF0njTQnHF0njTQnHEvPjmznHnYrHNYPdkknjDQgjTknHD1nRkknj7BpywbpyOMgjTknH70njTQnHbkP1mkrjwxr7qkudkknjDkgjTknHNOPHEdnWnYPj9YnHcvrj9LnWNLrjR0njTQn7kknjDYri33ri3zPB3znj-0njTQHyqlpyQ_mitdsWT92Dd6mv-8IAq1pj_9iyOYuyk9Hy7WcDqHc799nHKxnHKxPib9EgKkUARguyFspgEfPHnLsWnvca6si7wPHak9UA-ouiKZuyPoUzb9Ev6zUvd-s1NksWT8nWmvni3Qnjc9Nv7hmgFGs1N1Pz31P-kknjDdrHu0njTQsH70njTQsH70njTQEv6zUvd-gjTknHu6njm3uWDQsHF-Pj9VPjRBmzY3nHu6sHRBuhE1nWbQrAn1mk&v=2")
# get_item_detail_info("http://bj.ganji.com/meironghuazhuang/2145555660x.htm")
# get_item_detail_info("http://biz.click.ganji.com/bizClick?url=pZwY0jCfsvFJshI6UhGGshPfUiq-0MPCULRBpyGGmhR8uA-6UhO6UztznHnzP1DYrjDYXaOCIAd0njTQPNFaPj-DPHmYrNNQwWIDrj77njbOE1R7PbRDP1bdEYF0njTQPHbdPjNzn1EYrjEQnWm3rj0zPH03PRkknjDVgjTknHmOPWnLn1TYr7kknjDQP7kknjDznHnzP1DYrjDYgjTknHmOgjTknHEQgjTknHD1P-kknjDQn-kknjDQPjmYPWcQPH01nWcYgjTknH70njTQnHnQgjTknyFGuAwGUhI0njTQnRkknjDQrHTLPWT3P7t3gLKMgjTknHK0njTQPHbdPjNzn1EYrjEQnWm3rj0zPH03PRkknjDkgjTknHEOsW9OsWcvsWckrRkknj7PULGGUAQ6s1N8naTCHy7WpyOYULPCrzKFUMw-UaKPmyn9Hdn9yaTQn7tQn7td2iKK0ZK_uRI-mbVGIatdn108n1m92DVcRDdnsaK_pyV-cDI-mvVf2iKjpZFfUyNfPHT8na3zPWmQsWDknBKHmyu60hbfPHnLsWnvgjTknHN3P-kknjDVnRkknjDVnRkknj7jpZFfUyR0njTQmyNQuAEYmW9VPv7WPzYYPH03sH9zuWmVm1bkP16hPjnYnhEL&v=2")
# get_item_detail_info("http://biz.click.ganji.com/bizClick?url=pZwY0jCfsvFJshI6UhGGshPfUiqzpgFfUhIBmy-CIytfnWTOrHNLnH0LrZ98pZwVgjTknHIKrHIKnWmQrDPKwW7KnDRKnbujrDmvnNwDPW91rjndgjTknHNOPHEdnWnYPj9YnHcvrj9LnWNLrjR0njTQsRkknjDYrHnknjmknWK0njTQnHw0njTQnWTOrHNLnH0Lr7kknjDLn7kknjDvrRkknjDQn1N3gjTknHDzgjTknHDYPWEvnWDLPjTQP1R0njTQnRkknjDQn170njTQmh-buA-8udkknjDQgjTknHDOnj0vnj9Yg1wx0AI0njTQn7kknjDdrHNYPHc1PjE3PjDzPW93P1cdP19dgjTknHK0njTQPjb8rjb8nWm8nWTOgjTknNdfXh-_UADfPi3kca6PmyPGUMwf0v9ecD-8IAR_cDd6mzK5NzKmcjDkg1Dkg1NGcD7k0AQ-RvRBiv-Ys1N1Pz31PBTCiY6NHNk_cAQGpvN9wvRWpvtGcDPC0hqVuitdna3ksWcvPWD8nHTzc7P6uh7zpitdn108n1u0njTQP1DYgjTkniYQgjTkniYQgjTknNPC0hqVuRkknjD1uHEOmHPBnzYYmhw-sHw-nADVrjN3uBdBn1KBPvD3nyN3nyE&v=2")
# get_item_detail_info("http://bj.ganji.com/xuniwupin/2135542731x.htm")
# get_item_detail_info("http://biz.click.ganji.com/bizClick?url=pZwY0jCfsvFJshI6UhGGshPfUiqQpgw6ILRkpy3fnWDQn1c3PHDOrZ98pZwVgjTknH9Qn1D1nNczPN7DrjmYnWm1wHNQPjnLEND1E1IAn17jgjTknHNOPHEdnWnYPj9YnHcvrj9LnWNLrjR0njTQsRkknjDQP1DLP1mdgjTknHDYgjTknHcQnHnzrjNQrH60njTQP1K0njTQPjR0njTQnHNzgjTknHDzgjTknHDYPWEvnWD3PWmvnH-0njTQnRkknjDQn170njTQmh-buA-8udkknjDQgjTknHDOnj0vnj9Yg1ux0AI0njTQn7kknjDdrHNYPHc1PjE3PjDzPW93P1cdP19dgjTknHK0njTQPjb8rjb8nWm8nWTOgjTknNdfXh-_UADfPi3kca6PmyPGUMwf0v9ecD-8IAR_cDd6mzK5NzKmcjDkg1Dkg1NGcD7k0AQ-RvRBiv-Ys1N1Pz31PBTCiY6NHNk_cAQGpvN9wvRWpvtGcDPC0hqVuitdna3ksWcvPWD8nHTzc7P6uh7zpitdn108n1u0njTQPH9zgjTkniYQgjTkniYQgjTknNPC0hqVuRkknjDLrjbzuyDQridhuhmYsHw-nAnVmWD3miYOPAckrHu-PhE3rjb&v=2")
# get_item_detail_info("http://bj.ganji.com/ershoufree/2144659384x.htm")
# get_item_detail_info("http://bj.ganji.com/wupinjiaohuan/2138773890x.htm")
# get_item_detail_info("http://bj.ganji.com/xuniwupin/2109537646x.htm")
