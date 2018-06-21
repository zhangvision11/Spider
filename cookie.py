#coding = utf-8
import requests
from bs4 import BeautifulSoup
url = 'https://www.tapd.cn'
cookie = {'pgv_pvi':'5993169920','iteration_type_2000954971':'index',
'new_worktable':'todo%7C%7C%7Cexpiration_date',
'CAKEPHP':'b221689954736ce287d40167de902ed4baeba8664b2ec9d206fad1b1860a16fc',
'__root_domain_v':'.tapd.cn',' _qddaz':'QD.pnmqc8.vd0jb.jhfjnzy7','locale':'zh_cn',
't_u':'f426f668edc1fa48ccf8561e46878469c1162f28e1f048bd7b1bee62328fdec6c5a9c843103771690ed4283f1086cd4e48503bb57fdbd60a7bf406958e272caecae3a352456e811d%7C1',
't_cloud_login':'522075359%40qq.com'}
webdata = requests.get(url,cookies= cookie).text
soup = BeautifulSoup(webdata,'lxml')
print(soup)