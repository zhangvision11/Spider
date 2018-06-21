
#coding =utf -8
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306'


webdata = requests.get(url).text
soup = BeautifulSoup(webdata,'lxml')
dv = soup.select('')

