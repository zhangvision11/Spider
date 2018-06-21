#coding =utf -8
import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver


url = 'https://www.amazon.cn/s/ref=nb_sb_noss_1/461-8931868-9649465?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&url=search-alias%3Daps&field-keywords=%E8%A3%99%E5%AD%90'
webdata = requests.get(url).text

soup = BeautifulSoup(webdata,'html.parser')
dv_qunzi = soup.select('div.s-item-container > div.a-row.a-spacing-mini > div.a-row > a.a-link-normal.s-access-detail-page.s-color-twister-title-link.a-text-normal')

K =  soup.find_all('span',class_ ='a-size-base' )
price_list = [k.get_text() for k in K]
prd_list = [{'名字':n.get('title'), '链接': n.get('href')} for n in dv_qunzi]


for i in range(len(prd_list)):
    prd_list[i]['价格'] = price_list[i]

print(prd_list)